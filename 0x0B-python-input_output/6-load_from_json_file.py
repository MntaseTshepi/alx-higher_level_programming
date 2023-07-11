#!/usr/bin/python3
"""Defines a JSON function that creates objects"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename) as myfile:
        return json.load(myfile)
