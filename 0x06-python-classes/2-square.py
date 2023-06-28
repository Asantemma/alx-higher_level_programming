#!/usr/bin/python3
""" A square module"""


class Square:
    """declares the class"""

    def __init__(self, size=0):
        """initializes class fields

        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
