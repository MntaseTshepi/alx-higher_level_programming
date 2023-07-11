#!/usr/bin/python3
"""Defines an object to text file JSON function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to text file with JSON"""
    with open(filename, "w") as myfile:
        json.dump(my_obj, myfile)
