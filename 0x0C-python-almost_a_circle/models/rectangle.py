#!/usr/bin/python3
"""Childclass that inherits from Baseclass"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter property and get attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set values"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter property and get attributes"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set values"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter property and get attributes"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set values"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter property and get attributes"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set values"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Display method prints # to stdout"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Overide the __str__ method by returning
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                    self.__x, self.__y,
                                                    self.__width, self.__height)
