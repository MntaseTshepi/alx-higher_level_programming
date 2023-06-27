#!/usr/bin/python3
"""Defines a square class with a private attribute"""


class Square:
    """Represents a square class"""
    def __init__(self, size=0):
        """Initializes a square

        Args:
            size(int): Size of the square.
        """
        self.size = size

    @property
    """Get/set the current size of a square"""
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ Returns the current area of a square"""
        return (self.__size * self.__size)
