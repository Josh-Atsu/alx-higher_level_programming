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
    exit(1)

if not sys.argv[1].isdigit:
    print("N must be a number")
    exit(1)
if sys.argv[1].isdigit < 4:
    print("N must be at least 4")
    exit(1)
