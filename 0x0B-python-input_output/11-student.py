#!/usr/bin/python3
"""Defines a class that has a method toJSON"""


class Student:
    """This is the Class with public attributes"""

    def __init__(self, first_name, last_name, age):
        """Instantiating with parameters"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """retrieves a dictionary representation of a Student instance"""
        if attr is None:
            return self.__dict__
        new_dict = {}
        for name in attr:
            if name == "first_name":
                new_dict["first_name"] = self.first_name
            elif name == "last_name":
                new_dict["last_name"] = self.last_name
            elif name == "age":
                new_dict["age"] = self.age
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if not json:
            return
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
