#!/usr/bin/python3
"""This module defines a class MyInt"""


class MyInt(int):
    """Class that inverts the == and != operators on ints"""
    def __eq__(self, other):
        """Returns True if self != other"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
