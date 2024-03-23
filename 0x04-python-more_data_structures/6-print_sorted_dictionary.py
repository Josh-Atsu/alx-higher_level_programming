#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_d = []
    if a_dictionary:
        for a, b in a_dictionary.items():
            key_d.append(a)
        key_d.sort()
        for i in key_d:
            print("{}: {}".format(i, a_dictionar[i]))
