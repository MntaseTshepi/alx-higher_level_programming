#!/usr/bin/python3

def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary"""
    count = 0

    keys = a_dictionary.keys()

    for i in keys:
        count += 1

    return count
