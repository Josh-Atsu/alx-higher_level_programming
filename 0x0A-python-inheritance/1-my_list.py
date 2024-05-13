#!/usr/bin/python3
"""This class inherits from list and prints in ascending order"""


class MyList(list):
    """This class inherits from list"""
    def __init__(self):
        super().__init__

    def print_sorted(self):
        """Sort the array and print it in ascending order"""
        new_array = self[:]
        new_array.sort()
        print(new_array)
