#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = [0, 0]
    list_b = [0, 0]
    for i, a, b in enumerate(zip(tuple_a, tuple_b)):
        list_a[i] = a
        list_b[i] = b
        if i == 1:
            break
    return tuple(list_a[0] + list_b[0], list_a[1] + list_b[1])
