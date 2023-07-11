#!/usr/bin/python3
"""This module contains the is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True or False"""
    if type(obj) is a_class:
        return True
    else:
        return False
