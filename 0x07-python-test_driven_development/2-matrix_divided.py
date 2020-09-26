#!/usr/bin/python3
"""

Module
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    Error1 = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError(Error1)
    for i in matrix:
        if type(i) is not list:
            raise TypeError(Error1)
        if len(matrix[0]) is not len(i):
            raise TypeError('Each row of the matrix must have the same size')
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(Error1)
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]
    return new_matrix
