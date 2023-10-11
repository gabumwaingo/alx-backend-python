#!/usr/bin/env python3


import random
import asyncio


async def wait_random(max_delay = 10):
    """ generates a random delay between 0-10 """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
