#!/usr/bin/python3
"""Defines a square class with a private attribute"""

class Square:
    """Represents a square class"""
    def __init__(self, size=0):
        """Initializes a square

        Args:
            size(int): Size of the square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Returns the current area of a square"""
        return (self.__size * self.__size)
