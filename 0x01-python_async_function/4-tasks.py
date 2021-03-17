#!/usr/bin/env python3
'''Tasks'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Alter measure time def to take de list of
    delay values'''
    lst_t = []

    for _ in range(n):
        lst_t.append(task_wait_random(max_delay))

    return [await t for t in asyncio.as_completed(lst_t)]
