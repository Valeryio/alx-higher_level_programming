#!/usr/bin/python3
"""
    This module contains the base class of the project and all its attributes
"""
import json
from rectangle import Rectangle


class Base:
    """
        That is the basic class that we create for out project.

    Attributes:
        __nb_objects (int): this is a private attributes about the number of
        object have been instanciated from the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            This method is the constructor of the base class
        Args:
            id (int): a public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            This serialise a python object to a json object notation
        """
        data = ""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"

        data = json.dumps(list_dictionaries)

        return str(data)

    @classmethod
    def save_to_file(cls, list_objs):

        data = []
        filename = cls.__name__+'.json'

        with open(filename, 'w') as file:
            if list_objs is None:
                json.dump([], file)
            else:
                for i in list_objs:
                    data.append(i.to_dictionary())

                data = cls.to_json_string(data)
                file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """
            This method deserialise a python to a string
        """
        data = ""

        if json_string == [] or json_string is None:
            return []

        data = json.loads(json_string)
        return data

    @classmethod
    def create(cls, **dictionary):
        """
            This method creates an object from a dictionary
        """
#        print(f"DICT : {dictionary}")
        dummy = Rectangle(3, 5, 1)
#        print(dummy)
        dummy.update([1, 2, 3, 4], dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__+".json"

        with open(filename, "r+") as file:
            data = json.load(file)

            print(data)

