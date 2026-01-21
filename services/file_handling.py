import logging
import os

logger = logging.getLogger(__name__)

def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    end_signs = ",.!:;?"
    max_end = min(len(text), start + page_size)
    chunk = text[start:max_end]

    last_good = -1
    i = 0
    while i < len(chunk):
        if chunk[i] in end_signs:
            while i + 1 < len(chunk) and chunk[i + 1] in end_signs:
                i += 1
            seq_end = i

            after_seq = start + seq_end + 1
            if (
                after_seq == len(text)
                or text[after_seq].isspace()
                or text[after_seq].isalpha()
            ):
                last_good = seq_end
        i += 1

    if last_good != -1:
        page_text = chunk[: last_good + 1]
    else:
        page_text = chunk

    return page_text, len(page_text)


def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    try:
        with open(file=os.path.normpath(path), mode="r", encoding="UTF-8") as f:
            text = f.read()
    except Exception as e:
        logger.info("Error reading a book: %s", e)
        raise e
    start = 0
    num_of_page = 1
    book = {}
    all_size = len(text)
    while start < all_size:
        text_page, size = _get_part_text(text, start, page_size)
        book[num_of_page] = text_page.strip()
        num_of_page+=1
        start += size
    return book
