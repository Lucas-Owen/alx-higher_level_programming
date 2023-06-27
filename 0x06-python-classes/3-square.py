#!/usr/bin/python3
"""This module defines a Square Class"""
class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Initializes an instance with private member size
        
        Args:
            size (int): Size of the square

        Raises:
            TypeError: When passed size is not an int type
            ValueError: When size < 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the area of this square
        
        Returns:
            The area of the square
        """
        return self.__size * self.__size
