#!/usr/bin/python3
"""
Module 1-Base_Class
"""
import json


class Base:
    """
    class that will be de base of te other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        classmethod that writes the JSON string representation
        of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = class_name + ".json"
        result = []

        for obj in list_objs:
            result.append(cls.to_dictionary(obj))

        json_string = Base.to_json_string(result)

        with open(filename, mode="w", encoding="UTF-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the list of the JSON
        string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with all attributes already set.

        Args:
            cls: the class to create an instance of. It can be
                Rectangle or Square
            **dictionary: must be used as **kwargs of the method update
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        if cls.__name__ == "Square":
            dummy = cls(3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        ret = []
        try:
            with open("{}.json".format(cls.__name__), 'r') as file:
                str_list = file.read()
            dict_list = cls.from_json_string(str_list)
        except:
            dict_list = dict()
        for obj_dict in dict_list:
            new_obj = cls.create(**obj_dict)
            ret.append(new_obj)
        return(ret)
