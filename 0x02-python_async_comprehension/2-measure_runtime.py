#!/usr/bin/env python3
""" A coroutine that executes async_comprehension
four times in parallel using asyncio.gather and
measure the total runtime and return it
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of a coroutine running 4 times
    in parallel
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    approx_runtime = time.time() - start_time
    return approx_runtime
