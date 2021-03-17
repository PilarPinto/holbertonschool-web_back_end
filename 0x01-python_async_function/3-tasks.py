#!/usr/bin/env python3
'''Using regular function with
asynchronos'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Using asancy.Task create task await
    the completation of that
    '''
    return asyncio.create_task(wait_random(max_delay))
