#!/usr/bin/python3
"""This module defines matrix_divided

The function divides all elements of a given matrix by a given number
"""


def matrix_divided(matrix=None, div=None):
    """This function divides all elements of a matrix by a given divisor

    Args:
        matrix (list(list())): Matrix of numbers
        div (int or float): The divider
    Returns:
        list(list()): A new matrix containing the results of division to two
        decimal places
    Raises:
        ValueError: When matrix is not a valid matrix of numbers
        ZeroDivisionError: When div is 0
    """
    if type(matrix) is not list or not matrix or type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if {type(x) for row in matrix for x in row} | {int, float} != {int, float}:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if len({len(row) for row in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
