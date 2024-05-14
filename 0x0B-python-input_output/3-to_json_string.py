#!/usr/bin/python3
# 3-to_json_string.py
"""Defines a function that converts to json"""


import json
def to_json_string(my_obj):
    """import json and return the json representation of the string
    Args:
      my_obj: the string
    """
    return json.dumps(my_obj)
