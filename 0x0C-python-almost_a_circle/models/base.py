#!/usr/bin/python3
"""define a class Base"""


class Base:
    """BAse class with private class attribute initialized to 0"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor fir initialization"""
        if not id:
            self.id = id
        else:
            __nb_objects += 1
            id = __nb_objects
