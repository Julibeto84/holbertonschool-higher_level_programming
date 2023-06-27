#!/usr/bin/python3
"""
Definning a function wich appends a string.
"""


def append_write(filename="", text=""):
    """
    Appends string to the end
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
