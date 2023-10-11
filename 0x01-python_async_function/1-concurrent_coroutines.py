#!/usr/bin/env python3


import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Takes two ints n and max_delay
    spawns wait_random n times and stores delays in list
    """
    delay = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*tasks)
    return delay
