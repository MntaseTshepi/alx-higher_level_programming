#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    keys = a_dictionary.keys()

    for i in keys:
        if i == key:
            a_dictionary[i] = value

    a_dictionary.update({key: value})
    return a_dictionary
