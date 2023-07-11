#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student object

        Args:
            first_name (str): First name of student.
            last_name (str): Last name of student.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
