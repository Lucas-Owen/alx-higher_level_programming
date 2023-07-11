#!/usr/bin/python3
"""This module defines a function to read a file"""


def read_file(filename=""):
    """Reads a text file encoded in utf-8"""
    with open(filename, 'r') as f:
        for line in f:
            print(line)
