#!/usr/bin/env python3
'''Using a coruotine'''
import asyncio
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Async with random and generator'''
    for _ in range(10):
        await asyncio.sleep(1)
        ran_num = random() * 10
        yield ran_num
