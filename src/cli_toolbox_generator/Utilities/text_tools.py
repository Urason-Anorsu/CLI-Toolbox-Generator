import re
from unicodedata import normalize


def slugify(text: str) -> str:
    if not text:
        return "item"

    text = normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^0-9a-zA-Z]+", "_", text).lower()
    text = re.sub(r"_+", "_", text).strip("_")

    if not text:
        return "item"

    if text[0].isdigit():
        text = "_" + text

    return text
