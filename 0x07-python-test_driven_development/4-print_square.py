#!/usr/bin/python3
"""A function that prints a square with the character #"""


def print_square(size):
    """print the square with character #"""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        if i < size -1:
            print()
