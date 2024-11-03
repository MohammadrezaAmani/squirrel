import asyncio
import os
import time
from asyncio import Semaphore
from typing import List

import aiofiles
import aiohttp

from squirrel.cache import Cache
from squirrel.conf import ALLOWED_CONTENT_TYPES
from squirrel.utils import batch_list, extract_links, find_name, fix_url, valid_urls

global counter
counter = 0

start_time = time.time()


async def get_website(
    session: aiohttp.ClientSession,
    url: str,
    semaphore: Semaphore,
    test: bool = True,
) -> None | bytes:
    con = not test
    result = None
    async with semaphore:
        try:
            if test:
                async with session.head(url) as response:
                    content_type = response.headers.get("Content-Type", "")
                    con = True
                    if all(
                        [ctype_ not in content_type for ctype_ in ALLOWED_CONTENT_TYPES]
                    ):
                        con = False
            if con:
                async with session.get(url) as response:
                    response.raise_for_status()
                    global counter
                    counter += 1
                    print(
                        "\rsuccessfull:",
                        counter,
                        "time:",
                        time.time() - start_time,
                        end=" ",
                    )
                    result = await response.content.read()
        except Exception as _:
            pass
    return result


async def save_website(content: bytes, file_name: str, base_path: str):
    domain, page = find_name(file_name)
    path = f"{base_path}/{domain}"
    os.makedirs(path, exist_ok=True)
    count = "0" * (20 - len(str(counter))) + str(counter)
    async with aiofiles.open(f"{path}/{count}-{page}", "wb") as f:
        await f.write(content)


async def find_links(content: bytes, cache: Cache | None = None):
    links = extract_links(str(content))
    links = valid_urls(links)
    if cache:
        links = cache @ links
    cache += links
    return links


async def crawl_url(
    session: aiohttp.ClientSession,
    url: str,
    base_path: str,
    semaphore: Semaphore,
    batch_size: int = 100,
    test: bool = True,
    cache: Cache | None = None,
):
    content = await get_website(session, url, semaphore, test)
    if not content:
        return None

    await save_website(content, url, base_path)
    links = list(await find_links(content, cache))
    return await crawl(
        session,
        links,
        base_path,
        semaphore,
        batch_size,
        test,
        cache,
    )


async def crawl(
    session: aiohttp.ClientSession,
    urls: List[str],
    base_path: str,
    semaphore: Semaphore,
    batch_size: int = 100,
    test: bool = True,
    cache: Cache | None = None,
):
    for batched_urls in batch_list(urls, batch_size):
        tasks = [
            crawl_url(
                session, fix_url(url), base_path, semaphore, batch_size, test, cache
            )
            for url in batched_urls
        ]
        await asyncio.gather(*tasks)
