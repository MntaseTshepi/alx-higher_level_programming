#!/usr/bin/python3
"""Defines a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Intializes a square

        Args:
            size (int): The size of a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of a geometry"""
        return self.__size * self.__size
