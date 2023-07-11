#!/usr/bin/python3
"""Defines a string JSON function"""
import json


def to_json_string(my_obj):
    """JSON representation of an object"""
    return json.dumps(my_obj)
