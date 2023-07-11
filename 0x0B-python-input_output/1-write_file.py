#!/usr/bin/python3
"""This module defines a function to write text to a file (utf-8)"""


def write_file(filename="", text=""):
    """Writes text to filename encoded in utf-8"""
    with open(filename, 'w') as f:
        f.write(str(text))
