#!/usr/bin/python3
"""A magicclass that defines a circle from a bytecode"""

import math


class MagicClass:
    """
     Represents a class that performs mathematical operations on a circle.
    """
    def __init__(self, radius):
        """
        Initializes a MagicClass object with the given radius.

        Args:
            radius: The radius of the circle.

        Raises:
            TypeError: If radius is not a number (integer or float).
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            The circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
