#!/usr/bin/python3
"""This module defines a function that adds a new attribute to an object"""


def add_attribute(obj, name, value):
    """Adds an attribute to an object if possible"""
    if not isinstance(name, str) or '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
