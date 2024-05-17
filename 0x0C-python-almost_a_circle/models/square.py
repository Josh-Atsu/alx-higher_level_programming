#!/usr/bin/python3
"""models/square.py defines a class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter property and get attributes"""
        return self.width

    @size.setter
    def size(self, value):
        """Set values"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        if len(args) == 0:
            """Perform kwargs"""
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    self.id = value

    def to_dictionary(self):
        """Return a dictionary representation of the instance"""
        square_dict = {}
        square_dict["id"] = self.id
        square_dict["x"] = self.x
        square_dict["size"] = self.width
        square_dict["y"] = self.y
        return square_dict

    def __str__(self):
        """Overload __str__ and
        return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
