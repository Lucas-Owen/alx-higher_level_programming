#!/usr/bin/python3
"""This module defines a function to append to a file"""


def append_write(filename="", text=""):
    """Appends text to filename
    File is created if it does not exist
    """
    written = 0
    with open(filename, 'a', encoding='utf-8') as f:
        written = f.write(text)
    return written
