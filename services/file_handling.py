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
    book = {}

    return book 
