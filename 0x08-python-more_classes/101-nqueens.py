#!/usr/bin/python3
# N queens
"""
A The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard

a program that solves the N queens problem."""

import sys

len_arg = len(sys.argv)
if len_arg != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if sys.argv[1].isdigit() is False:
    print("N must be a number")
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)
