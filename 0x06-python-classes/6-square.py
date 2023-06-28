#!/usr/bin/python3
""" A Square module """


class Square:
    """ Declares the class """

    def __init__(self, size=0, position=(0, 0)):
        """Intializes attributes or fields

        Args:
            size: size of square
            position:  position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ sets attribute to be used in class """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Gets private instance attribute to be used in class """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ returns area of square """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
