#!/usr/bin/python3
"""models/square.py defines a class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overload __str__ and
        return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)
