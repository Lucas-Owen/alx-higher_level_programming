#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except TypeError as t:
        stderr.print("Exception: {}".format(t))
        return False
    return True
