#!/usr/bin/python3
"""
    This module contains the base class of the project and all its attributes
"""


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
