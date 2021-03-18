#!/usr/bin/env python3
'''Asynchornous comprenhension'''
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''collect 10 random numbers using an async comprehensing '''
    rand_nums = [ind async for ind in async_generator()]
    return rand_nums
