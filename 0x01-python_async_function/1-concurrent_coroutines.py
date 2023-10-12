#!/usr/bin/env python3


import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> list[float]:
    """
    Takes two ints n and max_delay
    spawns wait_random n times and stores delays in list
    """
    delays: list[float] = []
    tasks: list = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
