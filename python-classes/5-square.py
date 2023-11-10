#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Class will be used to create a objects that represent square."""
    def __init__(self, size=0):
        """Initialize a new square"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """Calculates the area of the square.."""
        return self.__size ** 2
    
    def my_print(self):

        """Print the square with the # character."""
        for idx, celda in enumerate(range(self.__size)):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
