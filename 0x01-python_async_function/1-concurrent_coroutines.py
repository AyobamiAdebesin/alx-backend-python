#!/usr/bin/env python3
""" Implementing concurrent coroutines """
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    return_values = []
    for i in range(n):
        return_values.append(await wait_random(max_delay))
    return return_values
