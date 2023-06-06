#!/usr/bin/python3
def remove_char_at(str, n):
    size = len(str)
    sr = ''
    for i in range(size):
        if i == n:
            continue
        sr += str[i]
    return sr
