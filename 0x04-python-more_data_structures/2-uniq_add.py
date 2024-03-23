#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    if my_list:
        for value in my_list:
            my_set.add(value)
    return sum(my_set)
