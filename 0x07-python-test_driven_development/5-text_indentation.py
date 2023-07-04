#!/usr/bin/python3
"""Defines a text-indentation function"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?' and ':'

    Args:
        text (string): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be string")

    j = 0
    while j < len(text) and text[j] == ' ':
        j += 1

    while j < len(text):
        print(text[j], end="")
        if text[j] == "\n" or text[j] in ".?:":
            if text[j] in ".?:":
                print("\n")
            j += 1
            while j < len(text) and text[j] == " ":
                j += 1
            continue
        j += 1
