IRAN_URLS = []
with open("./assets/domains.txt") as f:
    IRAN_URLS = f.read().split("\n")

FILE_NAME_SIZE = 12

ALLOWED_CONTENT_TYPES = ["html", "json"]
