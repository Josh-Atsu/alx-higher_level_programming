#!/usr/bin/python3
"""Defining a class for a sqaure and adding methods"""


class Square:
    """Initializing the class for data escapulating"""
    def __init__(self, size=0, position=(0, 0)):
        if size is not int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if position is not tuple(position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position
    """Private instances for both size and position"""

    """Add property for size"""
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """getter and setter for size with exception"""

    """adding property for position"""
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                value[0] < 0 or value[1] < 0 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 psitive integers")
        self.__position = value
    """The getter and setter for position with exception"""

    """Defining the area of the squaer"""
    def area(self):
        return (self.__size ** 2)
    """return the area of square"""

    """defining the special print method"""
    def my_print(self):
        n = self.__size
        if n == 0:
            print()
        else:
            for i in range(0, n):
                for y in range(0, self.__position[1]):
                    print("", end="")
                for y in range(0, self.__position[0]):
                    print(" ", end="")
                for x in range(0, n):
                    print("#", end="")
                print()
    """for my print method"""
