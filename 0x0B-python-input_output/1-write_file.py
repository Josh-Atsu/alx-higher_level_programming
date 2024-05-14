#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8)
and returns the number of characters written:"""


def write_file(filename="", text=""):
    """Use the permission write to write
    and overite the file if it exist"""
    with open("filename", encoding="utf-8") as myfile:
        my_read_file = myfile.read()

    with open(text, "w", encoding="utf-8") as my_file:
        writeChar = my_file.write(my_read_file)
        return writeChar
