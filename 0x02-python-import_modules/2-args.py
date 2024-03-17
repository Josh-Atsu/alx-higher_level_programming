#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_arg = len(argv)
    number = 0
    if num_arg == 1:
        print("{} arguments.".format(0))
    elif num_arg == 2:
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(num_arg - 1))
    for i in range(1, num_arg):
        number += 1
        print("{}: {}".format(number, argv[i]))
