#!/usr/bin/python3
"""Creating a class and defining it as a square
with printf method from ALX"""


class Square:
    """ Initializing the class
    and creating private instance"""
    def __init__(self, size):
        if size is not int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """Method for private instance"""

    """Methode fro defining area of the square"""
    def area(self):
        return (self.__size ** 2)
    """Return the area"""

    """Adding properties to the class"""
    @property
    def size(self):
        return (self.__size)
    """Returns the size of square"""

    """Now the setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """Having both Getters and setters"""

    """Creading a method the prints # on the stdout in the square format"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            n = self.__size
            for i in range(0, n):
                for x in range(0, n):
                    print("#", end="")
                print()
    """This the code for creating my _print"""
