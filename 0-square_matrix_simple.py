#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    return [[i**2 for row in matrix] for i in row]
