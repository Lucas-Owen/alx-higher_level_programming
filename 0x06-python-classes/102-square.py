#!/usr/bin/python3
"""This module defines a Square Class"""
class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Initializes an instance with private member size

        Args:
            size (int): Size of the square
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

    def __eq__(self, other):
        """Compare if two squares are equal

        Args:
            other (Square): The other square

        Returns: Bool
        """
        return self.size == other.size
    
    def __ne__(self, other):
        """Compare if two squares are not equal

        Args:
            other (Square): The other square

        Returns: Bool
        """
        return self.size != other.size
    
    def __lt__(self, other):
        """Compare if this square is less than other square

        Args:
            other (Square): The other square

        Returns: Bool
        """
        return self.size < other.size

    def __gt__(self, other):
        """Compare if this square is greater than other square

        Args:
            other (Square): The other square

        Returns: Bool
        """
        return self.size > other.size
    
    def __le__(self, other):
        """Compare if this square is less than or equal to
        other square

        Args:
            other (Square): The other square

        Returns: Bool
        """
        return self.size <= other.size

    def __ge__(self, other):
        """Compare if this square is greater than or equal to
        other square

        Args:
            other (Square): The other square

        Returns: Bool
        """
        return self.size >= other.size
