#!/usr/bin/python3
"""define a class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        my_list = [] 
        if list_objs is not None:
            for dict_n in list_objs:
                new_list = dict_n.to_dictionary()
                my_list.append(new_list)
        j_string = Base.to_json_string(my_list)
        with open(filename, "w", encoding="utf-8") as my_file:
            json.dump(j_string, my_file)
