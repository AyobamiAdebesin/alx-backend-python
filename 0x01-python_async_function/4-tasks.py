#!/usr/bin/env python3
""" Reimplementing an asynchronous function; wait_n, using asyncio.Task """
import asyncio


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Executing mutliple coroutines simultaneously """
    delay_values: List[float] = []
    return_values: List[float] = []
    for _ in range(n):
        delay_values.append(asyncio.create_task(wait_random(max_delay)))
    for delay in asyncio.as_completed(delay_values):
        first_arrived = await delay
        return_values.append(first_arrived)
    return return_values
