#!/usr/bin/python3
def roman_to_int(roman_string):
    test_string = roman_string.find("")
    if test_string < 0:
        return 0
    roman = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)
    sum_x = 0
    for i, letter in enumerate(roman_string):
        num = roman[letter]
        try:
            if num < roman[roman_string[i + 1]]:
                num = num * -1
        except IndexError:
            pass
        sum_x = sum_x + num
    return sum_x
