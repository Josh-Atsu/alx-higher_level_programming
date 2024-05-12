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
        max2 = max_integer([1, 2, 4, 3])
        self.assertEqual(max1, 4)
        self.assertEqual(max2, 4)

if __name__ == '__main__':
    unittest.main()
