#!/usr/bin/python3

def no_c(my_string):

    """Removes all characters c and C from a string"""

    new_string = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            new_string += letter
    return new_string
