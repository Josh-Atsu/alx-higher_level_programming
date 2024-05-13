#!/usr/bin/python3
""" This is a file that defines a funtion to check
if one is an instance of another"""


def is_kind_of_class(obj, a_class):
    """The function check if isinstance of"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
