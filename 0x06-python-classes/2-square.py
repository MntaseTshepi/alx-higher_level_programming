#!/usr/bin/python3

class Square:
    """ A square class with a private attribute with error handling"""
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
