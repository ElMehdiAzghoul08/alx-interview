#!/usr/bin/python3
"""returns a list of lists of integers representing the Pascal’s triangle of n
--Pascal's Triangle task"""


def pascal_triangle(n):
    """pascal_triangle function"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        current_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(current_row[j-1] + current_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
