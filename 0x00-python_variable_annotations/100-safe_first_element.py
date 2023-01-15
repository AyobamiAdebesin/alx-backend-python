#!/usr/bin/env python3
""" Annotating a function correctly """
from typing import Any, Union, Sequence, NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    if lst:
        return lst[0]
    else:
        return None