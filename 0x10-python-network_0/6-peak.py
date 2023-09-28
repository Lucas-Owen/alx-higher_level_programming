#!/usr/bin/python3
"""This module defines a function find_peak"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    Args:
        list_of_integers: list - List of integers
    Return:
        int - (The peak ) or None
    """
    # if not isinstance(list_of_integers, list):
    #     raise TypeError("list_of_integers should be a list")
    if not list_of_integers:
        return None
    # if {type(item) for item in list_of_integers} != {int}:
    #     raise TypeError("list_of_integers should be a list of integers")
    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    for i in range(1, size - 1):
        a = list_of_integers[i-1]
        b = list_of_integers[i]
        c = list_of_integers[i+1]
        if a <= b >= c:
            return b
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    return None
