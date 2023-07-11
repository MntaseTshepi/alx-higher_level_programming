#!/usr/bin/python3
"""Defines an object JSON function"""
import json


def from_json_string(my_str):
    """JSON representation of an object."""
    return json.loads(my_str)
