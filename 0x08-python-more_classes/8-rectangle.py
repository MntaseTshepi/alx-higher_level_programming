#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle class

    Attributes:
        number_of_instances (int): The number of rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle

        Args:
            width(int): The width of a rectangle.
            height(int): The height of a rectangle.
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with a bigger area

        Args:
            rect_1 (rectangle): The first rectangle.
            rect_2 (rectangle): The second rectangle

        Raises:
            TypeError: If either rect_1 or rect_2 is not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Returns the representaion of the rectangle using #"""

        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec += str(self.print_symbol)
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
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
