#!/usr/bin/env python3


import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ loops 10 times then returns a random num """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
