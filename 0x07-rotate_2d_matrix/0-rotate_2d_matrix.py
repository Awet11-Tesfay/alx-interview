#!/usr/bin/python3
""" Given an n X n 2D matrix rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """ Do not return anything
    """
    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(n):
            matrix[j].append(matrix[i].pop(0))
