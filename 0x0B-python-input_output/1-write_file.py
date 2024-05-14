#!/usr/bin/python3
# 1-write_file.py
"""Defines a function for writing"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
     filename: file to write into
     text: contains the string to write
     """
    with open(filename, "w" encoding="utf-8") as myfile:
        return myfile.write(text)
