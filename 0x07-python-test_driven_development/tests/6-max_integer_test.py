#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the max_integer function under all possible conditions
    """
    def test_normal(self):
        """Tests general expected cases
        """
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([1, 3, 5, 4, 2]), 5)
        self.assertEqual(max_integer([1, 3, 2, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -3, -5, -4, -2]), -1)
        self.assertEqual(max_integer([]), None)

    def test_invalid_types(self):
        """Tests cases when an error is expected
        """
        self.assertRaises(TypeError, max_integer, None)
        # self.assertRaises(TypeError, max_integer, ['one', 'two',
        # 'three', 'four'])
        # self.assertRaises(TypeError, max_integer, 'list')
        self.assertRaises(TypeError, max_integer, 1)
