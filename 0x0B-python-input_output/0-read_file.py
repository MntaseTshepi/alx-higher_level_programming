#!/usr/bin/python3
""" Defining a file-reading function"""


def read_file(filename=""):
    """Prints the stdout"""
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
