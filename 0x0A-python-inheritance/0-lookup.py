#!/usr/bin/python3
"""Defines a function that lists available attributes of an object"""
def lookup(obj):
    """Return a list of attributes of an object"""
    return dir(obj)
