#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    a function that prints a matrix of integers
    """
    for r in matrix:
        print(" ".join("{:d}".format(c) for c in r))
