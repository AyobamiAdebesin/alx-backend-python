#!/usr/bin/env python3
""" A function that returns an async.Task object """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Returns an async.Task object """
    task_object = asyncio.create_task(wait_random(max_delay))
    return task_object
