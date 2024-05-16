#!/usr/bin/python3
"""Childclass that inherits from Baseclass"""


class Rectangle(Base):
    """Class Rectangle that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__id = id

    @property
    def width(self):
        """Getter property and get attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set values"""
        self.__width = value

    @property
    def height(self):
        """Getter property and get attributes"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set values"""
        self.__height = value

    @property
    def x(self):
        """Getter property and get attributes"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Set values"""
        self.__x = value

    @property
    def y(self):
        """Getter property and get attributes"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set values"""
        self.__y = value
