#!/usr/bin/python3
"""
    6-max_integer.py module
"""


def max_integer(list=[]):
    """
        finds and returns the max integer in a list of integers
        If the list is empty, the function returns None

        Args:
            list (list): The list of integers.

    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
