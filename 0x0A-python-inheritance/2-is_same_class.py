#!/usr/bin/python3
"""This module defines a function that checks
if an object is of a certain class
"""


def is_same_class(obj=None, a_class=None):
    """Checks if an object is an exact instance of a class"""
    return type(obj) is a_class
