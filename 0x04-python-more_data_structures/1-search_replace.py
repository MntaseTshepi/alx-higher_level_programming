#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another"""

    cpy_list = my_list[:]

    for i in range(len(cpy_list)):
        if cpy_list[i] == search:
            cpy_list[i] = replace

    return cpy_list
