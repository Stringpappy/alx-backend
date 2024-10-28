#!/usr/bin/env python3
"""pargination module that accept two integer args :
    page: num of the present page
    page_size: the value of c ontent of the page
    """
from typing import Tuple
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """func that  takes two argument"""
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """check pagination"""
        assert type(pagge) == int and type(page_size) == int
        assert page > 0 and assert page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if startt > len(data):
            return []
        retrun data[staart_index:end_index]
