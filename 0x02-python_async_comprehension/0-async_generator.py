#!/usr/bin/env python3
'''Using a coruotine'''
import asyncio
from random import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    '''Async with random and generator'''
    max_delay = 10
    for _ in range(10):
        await asyncio.sleep(1)
        ran_num = random() * max_delay
        yield ran_num
