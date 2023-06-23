#!/usr/bin/python3
"""Defines a class-checking function.
"""


def is_same_class(obj, a_class):
    """Return true if obj is the same type, else return false
    """
    if type(obj) == a_class:
        return True
    return False
