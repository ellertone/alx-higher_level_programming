#!/usr/bin/python3
"""
This is the matrix division module.
The module prototype:  def matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of  a matrix
    Args:
        matrix(int, float) : a list of lists of integers or floats
        div (int, float) : dividend
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if isinstance(i, bool) or not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if isinstance(div, bool) or not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    matrix = [[round(i / div, 2) for i in row] for row in matrix]
    return matrix
