#!/usr/bin/python3
"""This module defines a function that checks if an object
is an instance of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class"""
    return isinstance(obj, a_class)
