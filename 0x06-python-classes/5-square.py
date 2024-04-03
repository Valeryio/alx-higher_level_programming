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
        return self.__size * self.__size

    @property
    def size(self):
        """ This property is a getter that return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ This property is a setter of the property <size>"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """This property print a square with the character <#>"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
