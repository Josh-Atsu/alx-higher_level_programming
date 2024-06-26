#!/usr/bin/python3
# a script that adds all arguments
# 7-add_item.py
"""Defines a script that adds all arguments to a Python list,
and then save them to a file:"""
import sys
import json


if __name__ == "__main__":
    save_to_json_file =\
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file

    try:
        py_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        py_list = []
    arguments = sys.argv[1:]
    for args in arguments:
        py_list.append(args)
    save_to_json_file(py_list, "add_item.json")
