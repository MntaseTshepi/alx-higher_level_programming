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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): The attributes to represent (optional)
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
