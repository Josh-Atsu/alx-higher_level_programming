#!/usr/bin/python3
def uppercase(str):
    for single in str:
        upper_case = single
        if ord(single) >= 97 and ord(single) <= 122:
            upper_case = chr(ord(single) - 32)
        print("{}".format(upper_case), end='')
    print()
