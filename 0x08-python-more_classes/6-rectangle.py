#!/usr/bin/python3
"""
Defines a class Rectangle"""


class Rectangle:
    """This represents a rectangle"""

    instance_count = 0

    def __init__(self, width=0, height=0):
        """initializing the rectangle objects"""
        self.width = width
        self.height = height
        Rectangle.instance_count += 1

    @property
    def width(self):
        """Getter for privste instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """prints rectangle with a string character"""
        str_ch = ""
        if self.__width != 0 and self.__height != 0:
            str_ch += "\n".join("#" * self.__width
                                for x in range(self.__height))
        return str_ch

    def __repr__(self):
        """ reproduces rectangle of string character"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a bye message"""
        Rectangle.instance_count -= 1
        print("Bye rectangle...")
