#!/usr/bin/python3
"""function returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
; otherwise False."""


def inherits_from(obj, a_class):
    """check if is a subclass of using issubclass"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
