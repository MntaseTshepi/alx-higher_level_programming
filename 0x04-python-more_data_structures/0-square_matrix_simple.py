#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers"""

    cpy_matrix = matrix[:]
    return (list(map(lambda x: list(map(lambda y: (y**2), x)), cpy_matrix)))
