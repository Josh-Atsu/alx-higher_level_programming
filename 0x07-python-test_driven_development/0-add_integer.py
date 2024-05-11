#!/usr/bin/python3
# A function that adds two numbers
"""Adds two numbers"""


def add_integer(a, b=98):
    """Adds two integers"""
    #if not isinstance(a, int):
        #raise TypeError("a must be an integer")
    if isinstance(a, float):
        a = int(a)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    return a + b
