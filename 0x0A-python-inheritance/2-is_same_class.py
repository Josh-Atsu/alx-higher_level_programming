#!/usr/bin/python3
""" A function that returns True
if the object is exactly an instance of the specified class
; otherwise False"""


def is_same_class(obj, a_class):
    """The function checks using isinstance method
    and returns true or false"""
    if type(obj) is a_class:
        return True
    else:
        return False
