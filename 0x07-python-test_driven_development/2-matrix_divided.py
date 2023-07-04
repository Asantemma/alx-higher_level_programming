#!/usr/bin/python3
"""2-matrix_divided module"""


def matrix_divided(matrix, div):
    """
        divides all elements of a matrix

        Args:
            matrix: matrix whose elements are to be divided
            div: divisor
        Return: new matrix with divided elements

    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    length = 0
    if type(matrix) is not list:
        raise TypeError(error)

    for block in matrix:
        if type(block) is not list:
            raise TypeError(error)

        for element in block:
            if type(element) is not int and type(element) is not float:
                raise TypeError(error)

        if len(block) != length and length != 0:
            raise TypeError("Each row of the matrix must have the same size")
        length = len(block)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
