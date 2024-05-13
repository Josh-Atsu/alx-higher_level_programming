#!/usr/bin/python3
"""The BaseGeometry and a method area"""


class BaseGeometry:
    """The Parentclass"""

    def area(self):
        """The area raises exception because its it not defined"""
        raise Exception("area() is not implemented")
