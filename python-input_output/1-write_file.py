#!/usr/bin/python3
"""
Definning a file reading function.
"""


def read_file(filename=""):
    """
    Prints the UTF8 file to stdout.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
