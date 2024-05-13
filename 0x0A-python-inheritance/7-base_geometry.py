#!/usr/bin/python3
"""The BaseGeometry and a method area
and method that validates"""


class BaseGeometry:
    """The Parentclass"""

    def area(self):
        """The area raises exception because its it not defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the arguments passed: value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
