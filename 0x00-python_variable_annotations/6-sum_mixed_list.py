#!/usr/bin/env python3
""" Performs summation on a list with different types """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Sums all element in a mixed list """
    return sum(mxd_list)
