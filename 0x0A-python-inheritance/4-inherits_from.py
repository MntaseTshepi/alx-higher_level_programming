#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Defines a class inheritance function

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with.

    Return:
        True - If there's a match.
        False - If there is none.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
