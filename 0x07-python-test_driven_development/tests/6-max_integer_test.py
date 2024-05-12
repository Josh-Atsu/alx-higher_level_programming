#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_len(self):
        self.assertTrue(len([0]) > 0)
        self.assertFalse(len([]) > 0)

    def test_max_integer(self):
        max1 = max_integer([1, 2, 3, 4])
        max2 = max_integer([1, 9, 4, 3])
        self.assertEqual(max1, 4)
        self.assertEqual(max2, 9)

    def test_negative(self):
        max2 = max_integer([1, -9, 4, 3])
        self.assertEqual(max2, 4)
        max1 = max_integer([-30, -8, -1])
        self.assertEqual(max1, -1)

    def test_exist(self):
        max = max_integer([2])
        self.assertIs(max)
        max_n = max_integer()
        self.assertIsNone(max_n)

if __name__ == '__main__':
    unittest.main()
