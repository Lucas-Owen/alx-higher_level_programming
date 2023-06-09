#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    weight = 0
    if my_list is None or not my_list:
        return 0
    for pair in my_list:
        total += pair[0] * pair[1]
        weight += pair[1]
    return total / weight
