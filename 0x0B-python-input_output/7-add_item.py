#!/usr/bin/python3
"""Defines a script that adds all arguments to a Python list,
and then save them to a file:"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys
import json

py_list = []
for i in sys.argv:
    my_list = load_from_json_file(i)
    py_list.append(my_list)
with open(add_item.json, "a", encoding="utf-8") as myfile:
    save_to_json_file(myfile, py_list)
