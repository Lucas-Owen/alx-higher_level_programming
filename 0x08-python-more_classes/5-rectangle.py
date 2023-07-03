#!/usr/bin/python3
"""This module defines a rectangle class
"""


class Rectangle():
    """A Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the width

        Args:
            value (int): New width
        Raises:
            TypeError
            ValueError
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets the height

        Args:
            value (int): New height
        Raises:
            TypeError
            ValueError
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of this Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of this Rectangle"""
        return 2 * self.width * self.height

    def __str__(self):
        """Returns a string representation of this Rectangle"""
        res = ('#' * self.width + '\n') * (self.height - 1)
        res += '#' * self.width
        return res

    def __repr__(self):
        """Returns a formal representation of this Rectangle
        that can be evaluated to a new rectangle by eval
        """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Detect when a rectangle is deleted"""
        print('Bye rectangle...')
