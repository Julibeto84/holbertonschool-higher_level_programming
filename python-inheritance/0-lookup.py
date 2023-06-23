#!/usr/bin/python3
"""
    Module to return a list of object attributes and methods
"""


def lookup(obj):
    """
        lookup - Return a list with object's attributes and method
        Arguments:
            obj - Object to bild the list with

        Return:
            made list.
    """
    return dir(obj)
