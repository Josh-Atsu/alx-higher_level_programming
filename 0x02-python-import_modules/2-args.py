#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv)
    number = 0
    if num_arg == 1:
        print("{} arguments".format(0))
    elif num_arg == 2:
        number += 1
        print("{} argument:".format(number))
        print("{}: {}".format(number, sys.argv[1]))
    else:
        print("{} arguments:".format(num_arg - 1))
        for i in range(1, num_arg):
            number += 1
            print("{}: {}".format(number, sys.argv[i]))
