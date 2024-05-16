#!/usr/bin/python3
"""define a class Base"""


class Base:
    """BAse class with private class attribute initialized to 0"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor fir initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
