#!/usr/bin/python3
"""This module defines a function print_square

The function prints a square to stdout with # character
"""


def print_square(size=None):
    """This function prints a square with # character

    Args:
        size (int): Length of the square
    Returns:
        None
    Raises:
        TypeError: When size is not an int
        ValueError: When size is less than 0
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        return
    print(('#' * size + '\n') * (size - 1), end='')
    print('#' * size)
