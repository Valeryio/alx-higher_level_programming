#!/usr/bin/python3

"""
    This module contains a class definition of a square that
    inherits from a rectanglle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        This is the implementation of the square
    Attributes:
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] + ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
            This function updates the attributes of the instance
        """
        attributes = ['id', 'size', 'x', 'y']

        if args is not None and len(args) != 0:

            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                for i in attributes:
                    if i == attr:
                        setattr(self, i, value)

    def to_dictionary(self):
        class_dict = {}
        attributes = ['id', 'x', 'size', 'y']
        values = [self.id, self.x, self.size, self.y]

        for attr, value in zip(attributes, values):
            class_dict[attr] = value

        return class_dict
