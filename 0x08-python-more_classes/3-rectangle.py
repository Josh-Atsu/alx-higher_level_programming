#!/usr/bin/python3
# adding the __str__ function
"""
The class Rectangle with getters and setters
and the perimeter and area method
the public instance method __str__
"""


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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter to retrieve the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter to set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defines the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the primeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        lenght = self.__width * 2
        breadth = self.__height * 2
        return lenght + breadth

    def __str__(self):
        """should print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print("#", end="")
            if i < self.__height - 1:
                print()
        return ""
