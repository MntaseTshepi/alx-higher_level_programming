#!/usr/bin/python3
"""Defines a base class"""
import json
import csv
import turtle


class Base:
    """Represents the base model

    This class will be the “base” of all other classes in this project.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base.

        Args:
            id (int): The identity of a new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list of dictionaries.

        Args:
            list_dictionaries (int): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of a list to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                jfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """A JSON representation of a string.

        Args:
            json_string (str): A JSON string rep of a list of dicts.
        Returns:
            if json_string is None or empty - an empty list.
            else - the list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cla(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes instantiated from a JSON file

        Reads from `<cls.__name__>.json`

        Returns:
            if file does not exist - an empty list.
            else - a list of instantiated classes
        """
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, "r") as jfile:
                list_dict = Base.from_json_string(jfile.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangles and squares using the turtle module.

        Args:
            list_rectangles (list): A list of rectangle objects to draw.
            list_squares (list): A list of square objects to draw.
        """

        tur = turtle.Turtle()
        tur.screen.bgcolor("#b7312c")
        tur.pensize(3)
        tur.shape("turtle")

        tur.color("#ffffff")
        for rec in list_rectangles:
            tur.showturtle()
            tur.up()
            tur.goto(rec.x, rec.y)
            tur.down()
            for i in range(2):
                tur.forward(rec.width)
                tur.left(90)
                tur.forward(rec.height)
                tur.left(90)
            tur.hideturtle()

        tur.color("#b5e3d8")

        for sqr in list_squares:
            tur.showturtle()
            tur.up()
            tur.goto(sqr.x, sqr.y)
            tur.down()
            for i in range(2):
                tur.forward(sqr.width)
                tur.left(90)
                tur.forward(sqr.height)
                tur.left(90)
            tur.hideturtle()

        turtle.exitonclick()
