#!/usr/bin/python3
"""This module defines a function that converts an object to json"""

import json


def to_json_string(my_obj):
    """Returns a JSON string representation of my_obj"""
    return json.dumps(my_obj)
