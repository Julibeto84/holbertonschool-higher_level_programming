#!/usr/bin/python3
"""
    Print square:
    This module prints a square using the # char
"""


def print_square(size):
    """
    print_square - prints a square using the # char

    Arguments:
        size (int): Square size
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
