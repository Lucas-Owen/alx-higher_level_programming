#!/usr/bin/python3
"""This module defines a function say_my_name

The function prints to stdout
"""


def say_my_name(first_name=None, last_name=""):
    """This function prints the first and last name to stdout
    in the format 'My name is <first name> <last name>'

    Args:
        first_name (str): First name
        last_name (str): Last name
    Returns:
        None
    Raises:
        TypeError: If it does not recieve strings
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
