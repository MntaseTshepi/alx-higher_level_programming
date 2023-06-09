#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle

        Args:
            width(int): The width of a rectangle.
            height(int): The height of a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the attribute"""
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get/set the height of the attribute"""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Returns the representaion of the rectangle using #"""

        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec += '#'
            if i != self.__height - 1:
                rec += '\n'
        return (rec)

    def __repr__(self):
        """Returns the string representation of the rectangle."""
        rec = "Rectangle(" + str(self.__width)
        rec += "," + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        """Prints a message when an instance is deleted"""

        print("Bye rectangle...")
