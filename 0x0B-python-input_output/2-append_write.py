#!/usr/bin/python3
# 2-append_write.py
""" Defines a function appending to a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added:

    Args:
      filename: name of the file to append text
      text: the string to append
    """
    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)
