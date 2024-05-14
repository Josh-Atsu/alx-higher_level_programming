#!/usr/bin/python3
# 4-from_json_string.py
"""Defines a function that changes from json string"""


import json


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string:
    Args:
      my_str: the string that represents JSON string
    """
    return json.loads(my_str)
