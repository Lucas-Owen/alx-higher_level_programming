#!/usr/bin/python3
"""Module for multiplying two matrices
"""

import numpy


def lazy_matrix_mul(m_a=[[]], m_b=[[]]):
    """Multiply two matrices and return the result

    Args:
        m_a (list(list())): First matrix
        m_b (list(list())): Second matrix
    Return:
        list(list): A new matrix
    Raises:
        ValueError
    """
    return numpy.matmul(m_a, m_b)
