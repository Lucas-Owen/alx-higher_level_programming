#!/usr/bin/python3
"""This module contains a function to read json object from file"""


import json


def load_from_json_file(filename):
    """Returns a python object loaded from file"""
    obj = None
    with open(filename, 'r') as f:
        obj = json.loads(f.read())
    return obj
