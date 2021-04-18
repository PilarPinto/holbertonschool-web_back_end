#!/usr/bin/env python3
'''File for test the utils file'''
from parameterized import parameterized
from utils import access_nested_map

import unittest


class TestAccessNestedMap(unittest.TestCase):
    '''Class Test Acces Map'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''Definition that test outputs vs expected'''
        self.assertEqual(access_nested_map(nested_map, path), expected)
