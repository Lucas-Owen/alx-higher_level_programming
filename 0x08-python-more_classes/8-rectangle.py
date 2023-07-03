#!/usr/bin/python3
"""This module defines a rectangle class
"""


class Rectangle():
    """A Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of this Rectangle"""
        res = (str(self.print_symbol) * self.width + '\n') * (self.height - 1)
        res += str(self.print_symbol) * self.width
        return res

    def __repr__(self):
        """Returns a formal representation of this Rectangle
        that can be evaluated to a new rectangle by eval
        """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Detect when a rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle based on area

        Args:
            rect_1 (Rectangle):
            rect_2 (Rectangle):
        Raises:
            TypeError
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_2
