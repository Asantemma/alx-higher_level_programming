#!/usr/bin/python3
""" A Square module """


class Square:
    """ Declares the class """

    def __init__(self, size=0):
        """
        Intializes attributes or fields

        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """Gets attribute to be used in class"""
        return self.__size

    @size.setter
    def size(self, value):
        """used to value of attributes"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns area of square """
        return self.__size * self.__size
