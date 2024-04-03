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
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not (isinstance(position, tuple) and len(position) == 2 and \
                position[0] >= 0 and position[1] >= 0 and \
                isinstance(position[0], int) and isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """ This property is a getter that return the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ This property is a setter of the property <size>"""
        if not (isinstance(position, tuple) and len(position) == 2 and \
                position[0] >= 0 and position[1] >= 0 and \
                isinstance(position[0], int) and isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """This property print a square with the character <#>"""
        if not self.__size:
            print("")

        for i in range(self.__size):
            if self.__position[1] < 0:
                for j in range(self.__position[0]):
                    print(" ", end="")

            for j in range(self.__size):
                print("#", end="")
            print("")
