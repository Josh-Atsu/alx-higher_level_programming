#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numerator = 0
        denominator = 0
        for sub in (my_list):
            numerator += sub[0] * sub[1]
            denominator += sub[1]
        return (numerator / denominator)
    else:
        return 0
