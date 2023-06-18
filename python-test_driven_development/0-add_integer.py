#!/usr/bin/python3
""" add_integer - adds 2 integers
    returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    Arguments:
        Datatypes
    Raises:
        TypeError (a): Must be an integer.
        TypeError (b): Must be an integer.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    """Returns an integer: the addition of a and b"""
    return (int(a) + int(b))
