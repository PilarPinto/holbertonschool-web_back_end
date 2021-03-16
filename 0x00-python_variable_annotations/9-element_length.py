#!/usr/bin/env python3
'''
Type an iterable object
'''
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Using an iterable with Sequence
    '''
    return [(i, len(i)) for i in lst]
