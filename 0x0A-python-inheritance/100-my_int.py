#!/usr/bin/python3
"""
Definition of class MyInt
"""


class MyInt(int):
    """Definition of class MyInt that inherits from int class"""

    def __eq__(self, other):
        """rebels equals sign and inverts it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """rebels not-equals and inverts it"""
        return int(self) == int(other)
