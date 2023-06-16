#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_matrix = matrix.copy()

    for row in range(len(nw_matrix)):
        nw_matrix[row] = list(map(lambda x: x ** 2, nw_matrix[row]))

    return nw_matrix
