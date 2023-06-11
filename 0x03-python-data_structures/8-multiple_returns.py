#!/usr/bin/python3

def multiple_returns(sentence):

    """Returns the length of the character and its first character"""
    if sentence is None:
        return (0, None)
    return (len(sentence), sentence[0])
