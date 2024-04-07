#!/usr/bin/python3

"""This module contains only one function, print_square()
    :param size
"""
    
def print_square(size):
    """
        This function prints a square
        return: Nothing
    """

    if not isinstance(size, (int, float)) :
        raise TypeError("size must be an integer")

    if round(size) < 0:
        raise ValueError("size must be >= 0")

    for i in range(round(size)):
        for j in range(round(size)):
            print("#", end="")
        print("")
