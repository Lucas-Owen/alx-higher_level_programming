#!/usr/bin/python3
"""This module defines a function that returns the
dictionary description for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns a copy of obj.__dict__"""
    return dict(obj.__dict__)
