#!/usr/bin/python3

""" Class that inherits from BaseGeometry class and Rectangle subclass """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle class """

    def __init__(self, size):
        """Initializing function
            Args:
                width: breadth of rectangle
                height: length of rectangle
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ returns area """
        return super().area()

    def __str__(self):
        """ string representation of square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
