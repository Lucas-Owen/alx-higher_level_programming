#!/usr/bin/python3
from sys import stderr
def safe_function(fct, *args):
    result = None
    try:
        result = fct(args)
    except Exception as e:
        stderr.print("Exception: {}".format(e))
    return result
