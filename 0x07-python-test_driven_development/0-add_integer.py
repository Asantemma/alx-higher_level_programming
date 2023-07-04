#!/usr/bin/python3
"""0-add_integer module"""


def add_integer(a, b=98):
    """
    Addition of two integers

    Args:
        a: integer 1
        b: integer 2

    Returns:
        a plus b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("a must be an integer")
    else:
        a, b = int(a), int(b)
        return a + b
