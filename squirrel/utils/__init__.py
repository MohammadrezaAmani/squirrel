import re
from typing import List, Tuple
from urllib.parse import urlparse
from uuid import uuid4

from squirrel.conf import FILE_NAME_SIZE, IRAN_URLS

ignore_list = (
    ".DOC",
    ".DOCX",
    ".PDF",
    ".TXT",
    ".ODT",
    ".RTF",
    ".JPG",
    ".JPEG",
    ".PNG",
    ".GIF",
    ".SVG",
    ".BMP",
    ".TIFF",
    ".MP4",
    ".AVI",
    ".MKV",
    ".MOV",
    ".WMV",
    ".MP3",
    ".WAV",
    ".AAC",
    ".FLAC",
    ".OGG",
    ".ZIP",
    ".RAR",
    ".7Z",
    ".TAR",
    ".GZ",
    ".PY",
    ".JS",
    ".HTML",
    ".CSS",
    ".PHP",
    ".JAVA",
    ".C",
    ".CPP",
    ".RB",
    ".CSV",
    ".XLS",
    ".XLSX",
    ".JSON",
    ".XML",
    ".SQL",
    ".DB",
    ".MDB",
    ".EXE",
    ".DLL",
    ".ISO",
    ".BIN",
    ".DMG",
)


def is_valid_url(url: str):
    parsed_url = urlparse(url)
    path = parsed_url.path
    if path.endswith("/"):
        path = path[:-1]
    if path.upper().endswith(ignore_list):
        return False

    if not is_persian_url(parsed_url.netloc):
        return False
    return True


def valid_urls(urls: List[str]) -> List[str]:
    return [url for url in urls if is_valid_url(url)]


def extract_links(html):
    link_pattern = r'href=["\']?([^"\'>]+)'
    links = re.findall(link_pattern, html)
    return links


def find_name(file_name: str) -> Tuple[str, str]:
    parsed_name = urlparse(file_name)
    path = (
        "-".join([part for part in parsed_name.path.split("/") if part.strip()])
        or "index"
    )
    path = (
        "".join([char for i, char in enumerate(path) if i < FILE_NAME_SIZE])
        + "-"
        + str(uuid4())
        + ".html"
    )
    return parsed_name.netloc, path


def batch_list(lst, batch_size):
    return [lst[i : i + batch_size] for i in range(0, len(lst), batch_size)]


def is_persian_url(url: str, ends_with: str = ".ir"):
    if url.endswith(ends_with) or url in IRAN_URLS:
        return True
    return False


def fix_url(url: str) -> str:
    if not url.startswith("http"):
        url = f"https://{url}/"
    return url
