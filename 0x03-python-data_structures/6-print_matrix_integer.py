#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            for column in row:
                print("{:d}".format(column), end=" "
                      if column != row[-1] else "\n")
    else:
        print()
