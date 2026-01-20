import logging
import os

logger = logging.getlogger(__name__)

def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    lst = [',', '.', '!', '?', ':', ';']
    idx=start
    idx_s = 0
    while idx<len(text) and idx < start+size:
        if text[idx] in lst:
            idx_s = idx
        idx+=1
    if idx_s<len(text)-1:
        if text[idx_s+1] in lst:
            for i in range(idx_s-2, start-1, -1):
                if text[i] in lst:
                    idx_s = i
                    break
    page_text = text[start:idx_s+1]
    page_size = len(page_text)
    return page_text, page_size

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
