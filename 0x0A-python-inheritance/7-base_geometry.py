#!/usr/bin/python3
"""
    This is the module of the BaseGeometry class
"""


class BaseGeometry():
    """
        This is the BaseGeometry class
    Attributes:
    def __int__(self):
        pass
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) == int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
