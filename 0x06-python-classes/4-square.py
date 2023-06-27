#!/usr/bin/python3

class Square:
    """ A square class with a private attribute with error handling"""
    def __init__(self, size=0):
        self.size = size

    @property
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
