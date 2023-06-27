#!/usr/bin/python3
"""This module defines a Square Class"""
class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes an instance with private member size

        Args:
            size (int): Size of the square
            position (tuple(int, int)): Coordinate of the square
        """
        self.size(size)

    def area(self):
        """Calculates and returns the area of this square
        
        Returns:
            The area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Getter for size
        
        Returns:
            self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for self.__size
        
        Args:
            value (int): Size of the square

        Raises:
            TypeError: When passed size is not an int type
            ValueError: When size < 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position
        
        Returns:
            self.__position
        """
        return self.__position

    @position.setter
    def position(self, position):
        """Setter for self.__position
        
        Args:
            position (tuple(int, int)): Position of the square

        Raises:
            TypeError: When position is not a tuple of two positive int
        """
        if (type(position) != tuple or len(position) != 2 or
            type(position[0]) != int or type(position[1] != int)):
            raise TypeError("position must be a tuple"
                            " of two positive integers")
        self.__position = position

    def my_print(self):
        """Prints this square instance"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print(' ')
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)