#!/usr/bin/python3
""" A square class with a private attribute with error handling"""


class Square:
    """ Represents a square class"""
    def __init__(self, size=0):
        """Initializes a square

        Args:
            size(int): Size of square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
