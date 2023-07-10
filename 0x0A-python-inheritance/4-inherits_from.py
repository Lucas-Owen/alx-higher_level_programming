#!/usr/bin/python3
"""This module defines a function that checks if an object
is only an instance of an inherited class
"""


def inherits_from(obj, a_class):
    """Checks if an object is only a subclass of a_class"""
    # This also works
    # return type(obj) is not a_class and isinstance(obj, a_class)
    return issubclass(obj, a_class)
