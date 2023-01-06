#!/usr/bin/env python3
""" Working with Python type annotations """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats as input and return the sum
    as a float
    """
    return sum(input_list)
