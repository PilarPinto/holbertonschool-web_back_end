#!/usr/bin/env python3
'''Asynchornous Paralel Comprehensions'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Coroutine that will execute async_comprehension
    four times in parallel'''
    ini = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for ind in range(4)))
    total_runtime = time.perf_counter() - ini
    return total_runtime
