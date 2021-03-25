#!/usr/bin/env python3
'''
Simple Helper Function
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' Return the size  realted to the range of indexes'''
    start = abs((page - 1) * page_size)
    end = page * page_size
    return (start, end)
