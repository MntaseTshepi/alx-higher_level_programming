#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""

    key_list = list(a_dictionary.keys())
    sort_key = sorted(key_list)

    for key in sort_key:
        print('{}: {}'.format(key, a_dictionary[key]))
