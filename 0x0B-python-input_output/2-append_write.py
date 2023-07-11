#!/usr/bin/python3
""" Defining a file appending function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file

    Args:
        filename (str): Name of text file.
        text (str): The text to append to the file.
    Return:
         The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)
