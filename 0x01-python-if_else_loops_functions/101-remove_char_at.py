#!/usr/bin/python3
def remove_char_at(str, n):
    rem = ""
    i = 0
    for x in str:
        if i != n:
            rem += str[i]
        i += 1
    return (rem)
