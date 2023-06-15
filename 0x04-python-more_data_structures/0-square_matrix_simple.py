#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    a function that computes the square value
    of all integers of a matrix.
    """

    matrix_square = []

    for i in matrix:
        square_num = list(map(lambda n: n ** 2, i))
        matrix_square.append(square_num)

    return matrix_square
