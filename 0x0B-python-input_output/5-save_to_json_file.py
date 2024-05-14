#!/usr/bin/python3
"""Defines a function that saves to JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """
    that writes an Object to a text file,
    using a JSON representation:
    Args:
      my_obbj: the object to change
      filename: the file to save the JSON string
    """
    with open(filename, "w", encoding="utf-8"):
        json.dump(my_obj, filename)
