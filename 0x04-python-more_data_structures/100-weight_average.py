#!/usr/bin/python3
from itertools import reduce
def weight_average(my_list=[]):
    total, weight = reduce(lambda x, y: (x[0] * y[0], x[1] + y[1]))
    return total / weight
