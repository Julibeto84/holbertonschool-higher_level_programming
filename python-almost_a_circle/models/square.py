#!/usr/bin/python3
"""
Module 3-Square
"""

from models.rectangle import Rectangle
"""
Importing Rectangle Class to be inherited
"""


class Square(Rectangle):
    """
    Class Square that inherit from Rectangle Class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for an instance of the class Square

        Args:
            size (for both width and height)
            x
            y
            id
        they must me inherited from Rectangle

        Methods:
            area: returns the area of the object Square
            display: prints in stdo the square using '#'
            update: uses *args and *kwargs
            to_dictionary: returns a dict representation of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overriding the __str__ method so that it returns a specific message
        """
        msg = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                self.width)
        return msg

    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter for size

        Args:
            size: the size of the square
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        method that assigns an argument (from *args or **kwargs)
        to each attribute

        Args:
            args: list of arguments, all ints
            kwargs: assigns a key/value argument to attributes
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
                if len(args) >= 2:
                    self.size = args[1]
                if len(args) >= 3:
                    self.x = args[2]
                if len(args) >= 4:
                    self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Method that returns the dictionary representation of a square,
        containing all its attributes in a specific order:
        id, x, size, y
        """
        dict_rep = {}
        dict_rep["id"] = self.id
        dict_rep["x"] = self.x
        dict_rep["size"] = self.size
        dict_rep["y"] = self.y
        return dict_rep
