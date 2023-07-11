#!/usr/bin/python3
"""This module defines a function that returns a list of lists of integers
representing pascal's triangle of n
"""


def pascal_triangle(n):
    res = []
    for i in range(0, n):
        base = []
        for j in range(i+1):
            if j == 0 or j == i:
                base.append(1)
            else:
                base.append(res[-1][j] + res[-1][j-1])
        res.append(base)
    return res
