#!/usr/bin/python3
"""
    This is the module of the BaseGeometry class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        This is the Square class
    Attributes:
        size (int): the size of the Square
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
