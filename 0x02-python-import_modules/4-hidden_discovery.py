#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all_func = dir()
    for i in range(0, len(all_func)):
        if all_func[i][0] != '_':
            print("{}".format(all_func[i]))
