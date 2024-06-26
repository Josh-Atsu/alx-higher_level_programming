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
        if self.__height == 0 or self.__width == 0:
            print()
            return
        for w in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        if len(args) == 0:
            """Perform kwargs"""
            for key, value in kwargs.items():
                if key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
                elif key == "id":
                    self.id = value

    def to_dictionary(self):
        """Convert to dictionary"""
        new_dict = {}
        new_dict.update({"x": self.__x,
                         "y": self.__y,
                         "id": self.id,
                         "height": self.__height,
                         "width": self.__width})
        return new_dict

    def __str__(self):
        """Overide the __str__ method by returning
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)
