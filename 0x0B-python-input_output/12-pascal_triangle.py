#!/usr/bin/python3
""" Defines Pascal's Triangle function"""


def pascal_triangle(n):
    """Representing the Pascal’s triangle of n

    Returns:
        A list of lists of integers
    """

    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) != n:
        tri = triangle[-1]

        temp = [1]
        for j in range(len(tri) - 1):
            temp.append(tri[j] + tri[j + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
