#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for row in matrix:
        new_mat.append(list(map(lambda x: x * x, row)))
    return new_mat
