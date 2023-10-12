#!/usr/bin/env python3


import time
import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    total_time = 0

    for _ in range(n):
        start_time = time.time()
        asyncio.run(wait_n(1, max_delay))
        end_time = time.time()
        total_time += end_time - start_time

    av_time = total_time / n
    return av_time
