#!/usr/bin/python3
""" A Square module """


class Square:
    """ Declares the class """

    def __init__(self, size=0):
        """Intializes the attributes or fields

        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """ sets the attribute to be used in class """
        return self.__size

    @size.setter
    def size(self, value):
        """used to chanfe value of attributes"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns area of square """
        return self.__size * self.__size

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("#" * self.__size)
