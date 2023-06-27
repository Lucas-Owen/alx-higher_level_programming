#!/usr/bin/python3
"""Contains code decoded from some python bytecode"""


import math


class MagicClass:
    """Code seems to describe a magic class of some sort"""
    def __init__(self, radius=0):
        """Looks like a circle to this point

        Args:
            radius (int, float): A number
        """
        self.radius = radius

    @property
    def radius(self):
        """Getter for radius

        Returns:
            int or float: The radius of the circle
        """
        return self.__radius

    @radius.setter
    def radius(self, radius):
        """Setter for radius

        Args:
            radius (int, float): A number

        Raises:
            TypeError: When radius is not a number
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Definitely a circle at this point

        Returns:
            float: The area of the circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computes the circumference of the circle

        Returns:
            float: The circumference of the circle
        """
        return 2 * math.pi * self.__radius
