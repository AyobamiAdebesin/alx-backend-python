#!/usr/bin/env python3
""" An implementation of asynchronous code """
import asyncio
import random


async def wait_random(max_delay=10):
    """ An asynchronous function(couroutine) that takes in an integer
    argument 'max_delay' and waits for a random delay between 0 and max_delay
    and eventually returns it
    """
    rand_no = random.random() * max_delay
    await asyncio.sleep(rand_no)
    return rand_no
