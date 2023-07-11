#!/usr/bin/python3
"""This module defines a function to convert a json string to an object"""


import json


def from_json_string(my_str):
    """Returns a python object parsed from json string"""
    return json.loads(my_str)
