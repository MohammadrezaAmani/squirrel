from asyncio import Semaphore

import aiohttp

from squirrel.cache import Cache
from squirrel.conf import IRAN_URLS
from squirrel.core import crawl


async def main(
    max_concurrent: int = 50,
    batch_size: int = 5,
    skip_test: bool = False,
    base_path: str = "./data",
):
    semaphore = Semaphore(max_concurrent)
    async with aiohttp.ClientSession() as session:
        await crawl(
            session=session,
            urls=IRAN_URLS,
            base_path=base_path,
            semaphore=semaphore,
            batch_size=batch_size,
            test=not skip_test,
            cache=Cache(),
        )
