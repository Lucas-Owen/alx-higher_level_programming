#!/usr/bin/python3
"""This module defines a function to append to a file"""


def append_write(filename="", text=""):
    written = 0
    with open(filename, 'a', encoding='utf-8') as f:
        written = f.write(text)
    return written
