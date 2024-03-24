#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        best = ""
        for value in a_dictionary:
            if a_dictionary[value] > score:
                score = a_dictionary[value]
                best = value
        return best
