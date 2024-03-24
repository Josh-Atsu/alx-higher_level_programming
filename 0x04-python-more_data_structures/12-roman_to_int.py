#!/usr/bin/python3
def roman_to_int(roman_string):
    test_string = roman_string.find("")
    if test_string < 0:
        return 0
    sum_x = 0
    for i in roman_string:
        if i == 'M':
            sum_x += 1000
        elif i == 'D':
            sum_x += 500
        elif i == 'C':
            sum_x += 100
        elif i == 'L':
            sum_x += 50
        elif i == 'X':
            sum_x += 10
        elif i == 'V':
            sum_x += 5
        elif i == 'I':
            sum_x += 1
    return sum_x
