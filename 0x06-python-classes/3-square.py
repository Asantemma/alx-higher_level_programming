#!/usr/bin/python3
"""A Square module"""


class Square:
    """ Declares the  class """

    def __init__(self, size=0):
        """Intializes class fields

        Args:
            size: size of square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of a square
        """
        return self.__size * self.__size
