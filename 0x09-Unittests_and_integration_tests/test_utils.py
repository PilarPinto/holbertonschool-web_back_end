#!/usr/bin/env python3
'''File for test the utils file'''
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch

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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''Capture the exception'''
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Class for obtain Json from a dummy context'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        '''Get the mocked json payload'''
        patcher = patch("utils.requests.get")
        mock_get = patcher.start()
        mock_get.return_value.ok = payload.get("payload")
        mock_get.return_value.json.return_value = payload
        res = get_json(url)
        self.assertEqual(res, payload)
        mock_get.stop()


class TestMemoize(unittest.TestCase):
    '''Testing for utils.memoize decorator'''
    def test_memoize(self):
        '''Testing for utils.memoize decorator by mocking a_method'''
        class TestClass:
            '''A class for testing'''
            def a_method(self):
                '''Return a number'''
                return 42

            @memoize
            def a_property(self):
                '''return propiety'''
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_a:
            mock_a.return_value = True
            test = TestClass()
            test.a_property
            test.a_property
            mock_a.assert_called_once()
