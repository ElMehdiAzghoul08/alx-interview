#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotate matrix clockwise"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
