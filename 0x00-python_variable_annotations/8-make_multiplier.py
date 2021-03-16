#!/usr/bin/env python3
'''
Type annotated function that takes a float numer and return
the mult of that number with another float
using callable
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Takes a float param and multiplies it with some float
    '''
    def multip(multi):
        '''Def that operates the numbers'''
        return multi * multiplier
    return multip
