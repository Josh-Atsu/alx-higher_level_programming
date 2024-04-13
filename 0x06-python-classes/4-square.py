#!/usr/bin/python3
"""
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """


class Square:
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
        """
    def __init__(self, size=0):
        if size is not int(size):
            raise TypeError("size must be an integer")
            return
        elif size < 0:
            raise ValueError("size must be >= 0")
            return
        self.__size = size
    """
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """

    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """
    def area(self):
        area_s = self.__size ** 2
        return (area_s)
    """
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """

    """python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """
    @property
    def size(self):
        return (self.__size)
    """
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """

    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
            return
        if value < 0:
            raise ValueError("size must be >= 0")
            return
        self.__size = value
    """
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """