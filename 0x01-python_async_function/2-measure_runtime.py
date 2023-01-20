#!/usr/bin/env python3
""" Measuring the runtime of asynchronous operation """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay) -> float:
    """ Measure the runtime of an asynchronous operation """
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time: float = time.perf_counter() - start_time
    return elapsed_time/n
