#!/usr/bin/env python3
'''
execute multiple coroutines at the
same time with async
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Retunr the list of the values of delay'''
    lst_t = []
    lst_delay = []

    for _ in range(n):
        lst_t.append(asyncio.create_task(wait_random(max_delay)))
    for t in asyncio.as_completed(lst_t):
        lst_delay.append(await t)
    return lst_delay
