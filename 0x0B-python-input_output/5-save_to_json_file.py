#!/usr/bin/python3


"""This module defines a function to write an object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes my_obj to filename as a json string"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
