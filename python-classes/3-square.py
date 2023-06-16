#!/usr/bin/python3
""" Square - First python classes's class """


class Square:
    """ Init method to instantiate """
    def __init__(self, size=0):
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ Area - Calcs the area of the square """
    def area(self):
        area = self._Square__size ** 2
        return area
