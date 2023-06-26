#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as t:
        stderr.write("Exception: {}\n".format(t))
        return False
    return True
