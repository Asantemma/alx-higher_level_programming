#!/usr/bin/python3
"""function 4-inherits_from.py"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
