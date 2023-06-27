#!/usr/bin/python3
"""Defines square class with the private attribute size"""

class Square:
    """Represents a square class"""
    def __init__(self, size):
        """Initializes a square

        Args:
            size(int): Size of the square.
        """
        self.__size = size
