#!/usr/bin/python3
"""This module defines a rectangle class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry')


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width=1, height=1):
        """Initializer with width and height"""
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height

    def area():
        return self.__width * self.__height

    def __repr__(self):
        return f'{[self.__name__]} {self.__width}/{self.__height}'
