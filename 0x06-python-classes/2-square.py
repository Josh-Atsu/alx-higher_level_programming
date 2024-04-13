#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """


class Square:
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'
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
