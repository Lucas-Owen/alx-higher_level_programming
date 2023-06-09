#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns a new list same length as my_list with True False
    for numbers divisible or not divisible by 2
    
    args:
        my_list - List of integers
    """
    return [x % 2 == 0 for x in my_list]
