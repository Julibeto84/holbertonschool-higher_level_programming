#!/usr/bin/python3
"""
    Say my name:
    Module wich prints a name
"""


def say_my_name(first_name, last_name=""):
    """
        say_my_name - prints My name is <first name> <last name>
    
        Arguments:
            first_name (str): First name to print.
            last_name (str): Last name to print. Can be blank
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
