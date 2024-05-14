#!/usr/bin/python3
"""A function to lead from json string"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”:
    Args:
      filename: the JSON file
    """
    with open(filename, encoding="utf-8") as myfile:
        json.load(myfile)
