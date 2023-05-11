#!/usr/bin/python3
""" Given an n X n 2D matrix rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """ Do not return anything
    """
    x = len(matrix[0])

    for i in range(x - 1, -1, -1):
        for j in range(x):
            matrix[j].append(matrix[i].pop())
