#!/usr/bin/python3
"""This module defines a function to write text to a file (utf-8)"""


def write_file(filename="", text=""):
    """Writes text to filename encoded in utf-8"""
    written = 0
    with open(filename, 'w', encoding='utf-8') as f:
        written = f.write(str(text))
    return written
