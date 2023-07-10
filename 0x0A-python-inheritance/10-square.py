#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size=1):
        """Initializer with width and height"""
        Rectangle.__init__(self, size, size)
