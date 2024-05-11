#!/usr/bin/python3
#initialization adding getters and setters
""" The class Rectangle with getters and setters """


class Rectangle:
    """ The class Rectangle """

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter to retrieve the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter to set the value of width"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter to retrieve the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter to set the value of height"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value
