#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for i in my_string:
        alph = ord(i)
        if alph != ord('c') and alph != ord('C'):
            new_string += i
    return new_string
