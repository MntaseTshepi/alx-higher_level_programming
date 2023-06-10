#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    """Replaces an element of a list at a specific position"""

    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        cpy_list = my_list[:]
        cpy_list[idx] = element
        return cpy_list
