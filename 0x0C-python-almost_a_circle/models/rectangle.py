#!/usr/bin/python3
"""
Contains Rectangle Module
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle subclass which implements Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constractor

        args:
            width: width of rectangle
            height: height of rectangle
            x: init variable
            y: init variable
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """return area of width & height"""
        return self.width * self.height

    def update(self, *args, **kwargs):
        """update attributes"""
        if args:
            listme = ['id', 'width', 'height', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, listme[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def display(self):
        """prints rectangle with char # to stdout
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """prints method"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def to_dictionary(self):
        """returns dictonary representation of Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.integer_validator2('x', value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.integer_validator2('y', value)
        self.__y = value
