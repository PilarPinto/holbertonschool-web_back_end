#!/usr/bin/env python3
'''
Mixed List using
type annotation
'''
from typing import Union, List

mxd_lst = Union[int, float]


def sum_mixed_list(arr: List[mxd_lst]) -> float:
    '''
    Sum the elements of an list
    that has differen types (int & floats)
    '''
    return sum(arr)
