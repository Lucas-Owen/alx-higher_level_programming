#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [map(lambda row: [i**2 for i in row], matrix)]
