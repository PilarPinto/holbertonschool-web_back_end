#!/usr/bin/env python3
'''
Complex types
String and int float to tuple
'''
from typing import Union, Tuple

V = Union[int, float]


def to_kv(k: str, v: V)-> Tuple[str, float]:
    '''
    Definition that takes two different arguments
    k: string
    v: Could be int or float
    return a Tuple with double of v
    '''
    return(k, v**2)
