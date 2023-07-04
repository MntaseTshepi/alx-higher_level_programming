#!/usr/bin/python3
"""Defines a square printing function"""


def print_square(size):
    """Prints a square with a # character

    Args:
        size(int): Size of a square.

    Raises:
        TyperError: If size is not an integer.
        ValueError: If size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
