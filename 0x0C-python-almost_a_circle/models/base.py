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
        if list_dictionaries is None or list_dictionaries == []:
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
            my_file.write(j_string)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string
        representation json_string"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 4)
        else:
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as my_file:
                j_string = my_file.read()
        except FileNotFoundError:
            return []
        my_list = []
        obj_list = Base.from_json_string(j_string)
        for obj in obj_list:
            obj_1 = cls.create(**obj)
            my_list.append(obj_1)
        return my_list
