#!/usr/bin/env python3
""" Annotating a function correctly """
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return the first element of a Sequence """
    if lst:
        return lst[0]
    else:
        return None
