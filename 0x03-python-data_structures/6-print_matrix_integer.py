#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print('{:d}'.format(row), end='')
        print('{:s}'.format('\n'), end='')