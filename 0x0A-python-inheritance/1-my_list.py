#!/usr/bin/python3
"""Defines a MyList class"""


class MyList(list):
    """A class that inherits from list class"""
    def print_sorted(self):
        """Prints this list in sorted order"""
        print(sorted(self))
