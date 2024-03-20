#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        n = 0
        for i in matrix:
            for x in matrix[n]:
                print("{:d}".format(x), end=' ' if x != matrix[n][-1] else '')
            print()
            n += 1
