#!/usr/bin/env python3
"""pargination module that accept two integer args :
    page: num of the present page
    page_size: the value of c ontent of the page
    """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """func that  takes two argument"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
