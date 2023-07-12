#!/usr/bin/python3
"""
Contains inherited class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Representation of a square class
        Args:
            size: size of square side
    """
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of a square"""
        return self.__size ** 2
