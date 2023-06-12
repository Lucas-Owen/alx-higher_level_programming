#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns a new list same length as my_list with True False
    for numbers divisible or not divisible by 2
    args:
        my_list (list): List of integers
    Returns: list
        A list containing True and False corresponding to the
        indices of numbers divisible and not divisible by 2 in my_list
    """
    return [x % 2 == 0 for x in my_list]
