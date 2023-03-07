#!/usr/bin/env python3
""" Unittest for utils.acces_nested_map """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """ Perform unittest for utils.access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, answer: Any):
        """ Testing what the method is supposed to return """
        self.assertEqual(access_nested_map(nested_map, path), answer)
        
# if __name__ == "__main__":
#     unittest.main()
