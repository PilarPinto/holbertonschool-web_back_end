#!/usr/bin/env python3
'''
Using list of floats
and type annotated
'''
from typing import List

Input_list = List[float]


def sum_list(input_list: Input_list) -> float:
    '''
    Sum the elements of an input
    vector
    '''
    return sum(input_list)
