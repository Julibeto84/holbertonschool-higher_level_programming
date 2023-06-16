#!/usr/bin/python3
""" Add integer
    This modlue adds two numbers """


def add_integer(a, b=98):
    """ Arguments:
        a: First number to add (int or float)
        b: Second number to add (int or float)

    Returns:
        int: The sum of both numbers casted to intigers.
        TypeError if a or b is not a number
    """

    if isinstance(a, int) is False and isinstance(a, float) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False and isinstance(b, float) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
