#!/usr/bin/python3
"""This is a module that contains the function 7-base_geometry.py
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle and
       Class that inherits from BaseGeometry module
    """
    def __init__(self, width, height):
        """Initializing function
            Args:
                width: width
                height: height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
