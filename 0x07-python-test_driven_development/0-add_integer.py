#!/usr/bin/python3
"""This module defines add_integer
    The function adds two numbers as integers
    If a float is passed, the float is cast to an int
    Always returns an integer on success, raises an exception on failure
"""


def add_integer(a=0, b=98):
    """This function adds two integers

    Args:
        a (int): First number
        b (int): Second number
    Returns:
        The sum of a and b
    Raises:
        ValueError: When either a or b is not an integer
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise ValueError("a must be an integer")
    if type(b) is not int:
        raise ValueError("b must be an integer")
    return a + b
