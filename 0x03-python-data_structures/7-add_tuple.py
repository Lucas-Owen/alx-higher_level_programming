#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result_list = [0, 0]
    for i, a in zip(range(2), tuple_a):
        result_list[i] += a
    for i, b in zip(range(2), tuple_b):
        result_list[i] += b
    return tuple(result_list)
