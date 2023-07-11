#!/usr/bin/python3
"""This module defines a function that returns a list of lists of integers
representing pascal's triangle of n
"""


def pascal_triangle(n):
    res = []
    for i in range(1, n):
        l = []
        for j in range(i+1):
            if j == 0 or j == i:
                l.append(1)
            else:
                l.append(res[-1][j] + res[-1][j-1])
        res.append(l)
    return res
