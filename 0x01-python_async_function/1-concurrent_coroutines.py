#!/usr/bin/env python3
""" Implementing concurrent coroutines """
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Executing mutliple coroutines simultaneously """
    delay_values: List[float] = []
    return_values: List[float] = []
    for _ in range(n):
        delay_values.append(await wait_random(max_delay))
    for delay in asyncio.as_completed(delay_values):
        first_arrived = await delay
        return_values.append(first_arrived)
    return return_values
