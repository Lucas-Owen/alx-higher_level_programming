#!/usr/bin/python3
"""This module defines a function to append to a file"""


def append_write(filename="", text=""):
    written = 0
    with open(filename, 'a') as f:
        written = f.write(str(text))
    return written
