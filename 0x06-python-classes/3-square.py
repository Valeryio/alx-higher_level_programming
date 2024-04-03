#!/usr/bin/python3
"""
    This is a module for a square
"""


class Square:
    """This is an empty class of square

    Note:
    Args:
    Attributes:
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size
