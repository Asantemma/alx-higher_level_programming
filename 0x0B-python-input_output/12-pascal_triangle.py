#!/usr/bin/python3
"""
pascal_triangle module.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
        Args:
            n: number of lists and digits
        Returns: list of lists of integers

    """
    rows = [[1 for x in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
