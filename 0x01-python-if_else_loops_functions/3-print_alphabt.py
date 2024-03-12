#!/usr/bin/python3
for alp in range(97, 123):
    if alp in [101, 113]:
        continue
    print("{}".format(chr(alp)), end='')
