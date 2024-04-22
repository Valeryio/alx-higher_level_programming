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
