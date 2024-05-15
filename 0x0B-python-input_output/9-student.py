#!/usr/bin/python3
"""Defines a class that has a method toJSON"""


class Student:
    """This is the Class with public attributes"""

    def __init__(self, first_name, last_name, age):
        """Instantiating with parameters"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
