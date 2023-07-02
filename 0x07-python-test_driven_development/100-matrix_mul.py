#!/usr/bin/python3
"""Module for multiplying two matrices
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices and return the result

    Args:
        m_a (list(list())): First matrix
        m_b (list(list())): Second matrix
    Return:
        list(list): A new matrix
    Raises:
        TypeError
        ValueError
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if {type(x) for x in m_a} != {list}:
        raise TypeError("m_a must be a list of lists")
    if {type(x) for x in m_b} != {list}:
        raise TypeError("m_b must be a list of lists")
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    if {type(x) for row in m_a for x in row} | {int, float} != {int, float}:
        raise TypeError("m_a should contain only integers or floats")
    if {type(x) for row in m_b for x in row} | {int, float} != {int, float}:
        raise TypeError("m_b should contain only integers or floats")
    if len({len(row) for row in m_a}) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len({len(row) for row in m_b}) != 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    b_trans = [list(row) for row in zip(*m_b)]
    return [[sum(x*y for x, y in zip(row_a, row_b)) for row_b in b_trans]
            for row_a in m_a]
