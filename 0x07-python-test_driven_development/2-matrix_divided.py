#!/usr/bin/python3
# A function that divides the elemens of a matrix
"""Divides Element Of a matrix"""


def matrix_divided(matrix, div):
    """Divides element of a matrix
    args:
      matrix: list representation containing integers or float
      div: number to be divided by"""
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 2:
        if len(matrix[0]) != len(matrix[1]):
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(num, int) for num in matrix[0]):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    my_array = []
    for array in matrix:
        inner_array = []
        for i in array:
            num = i / div
            inner_array.append(round(num, 2))
        my_array.append(inner_array)
    return my_array
