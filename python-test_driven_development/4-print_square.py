#!/usr/bin/python3
"""
Definning a funtion wich print entire name properly.
"""


def print_square(size):
    """
    Prints a square with the # char.
    Arguments:
        size
    Raises:
        TypeError  (size): Size must be an integer.
        TypeError  (size): Size must be an integer.
        ValueError  (< 0): Size must be >= 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is True:
        raise TypeError("size must be an integer")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
