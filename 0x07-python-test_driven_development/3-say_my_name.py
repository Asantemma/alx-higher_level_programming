#!/usr/bin/python3
"""
    3-say_my_name Module
"""


def say_my_name(first_name, last_name=""):
    """
        Prints My name is <first_name> <last_name>

        Args:
            first_name: first name
            last_name: second name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
