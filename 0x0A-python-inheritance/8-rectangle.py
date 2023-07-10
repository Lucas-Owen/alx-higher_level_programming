#!/usr/bin/python3
"""This module defines a rectangle class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width=None, height=None):
        """Initializer with width and height"""
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height
