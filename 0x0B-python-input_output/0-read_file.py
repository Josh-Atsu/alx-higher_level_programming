#!/usr/bin/python3
"""a function that reads a text file (UTF8)
and prints it to stdout:"""


def read_file(filename=""):
    """Opens filename, read and print to stdout"""
    with open(filename, encoding="utf-8") as myfile:
        for line in myfile.readlines():
            print("{}".format(line), end="")
