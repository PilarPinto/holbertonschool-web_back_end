#!/usr/bin/env python3
'''
First element of a sequence
The types of the elements of the
input are not know
'''
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Using Sequence and union
    to declare a set of possible inputs [Any]
    '''
    if lst:
        return lst[0]
    else:
        return None
