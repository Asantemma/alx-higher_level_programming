#!/usr/bin/python3
"""A module that contains a class MyList that inherits from list"""


class MyList(list):
    """A subclass of list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
