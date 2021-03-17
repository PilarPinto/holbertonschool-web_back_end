#!/usr/bin/env python3
'''Using a coruotine'''

import asyncio
from random import random


async def wait_random(max_delay=10):
    '''Asyn with random'''
    ran_num = random() * max_delay
    await asyncio.sleep(ran_num)
    return ran_num
