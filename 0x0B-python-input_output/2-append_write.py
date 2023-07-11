#!/usr/bin/python3
"""This module defines a function to append to a file"""


def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        f.write(str(text))
