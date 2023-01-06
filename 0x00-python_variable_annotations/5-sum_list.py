#!/usr/bin/env python3
""" Working with Python type annotations """


def sum_list(input_list: list[float]) -> float:
    """
    Takes a list of floats as input and return the sum
    as a float
    """
    return float(sum(input_list))
