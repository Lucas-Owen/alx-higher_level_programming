#!/usr/bin/python3
"""This module defines a rectangle class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width=None, height=None):
        """Initializer with width and height"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __repr__(self):
        return f'[Rectangle] {self.__width}/{self.__height}'

    def __str__(self):
        return self.__repr__()
