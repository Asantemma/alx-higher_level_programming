#!/usr/bin/python3
"""
    4-print_square Module
"""


def print_square(size):
    """
        Prints a square with the character '#'

        Args:
            size: length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float:
        raise TypeError("size must be an integer")

    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()
