#!/usr/bin/python3
""" Defining a file writing function"""


def write_file(filename="", text=""):
    """Writes a string to a text file

    Args:
        filename (str): Name of text file.
        text (str): The text to write to the file.
    Return:
         The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as myfile:
        return myfile.write(text)
