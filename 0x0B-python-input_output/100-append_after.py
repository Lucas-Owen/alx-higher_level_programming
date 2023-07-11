#!/usr/bin/python3
"""This module defines a function that inserts a line of
text to a file after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after a line containing search_string"""
    lines = []
    with open(filename, 'r') as f:
        lines = f.getlines()
    to_write = []
    for line in lines:
        to_write.append(line)
        if line.find(search_string) > 0:
            to_write.append(new_string)
    with open(filenam, 'w') as f:
        for line in to_write:
            f.write(line)

