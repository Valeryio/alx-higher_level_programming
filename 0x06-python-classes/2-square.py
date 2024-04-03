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
        try:
            my_size = int(size)
            if my_size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = int(size)

        except TypeError:
            print("size must be an integer")
