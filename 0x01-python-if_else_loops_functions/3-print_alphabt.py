#!/usr/bin/python3
for a in range(97, 123):
    if a != 101 | a != 113:
        print("{}".format(chr(a)), end='')
