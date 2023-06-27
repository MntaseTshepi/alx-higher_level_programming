#!/usr/bin/python3
"""Defines a square class with a private attribute"""


class Square:
    """Represents a square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square

        Args:
            size(int): Size of a square
            position(int, int): The position of a square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the attribute"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")

        if (not all(isinstance(digit, int) for digit in value) or
                not all(digit >= 0 for digit in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ Returns the current area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints out a square with #"""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()
