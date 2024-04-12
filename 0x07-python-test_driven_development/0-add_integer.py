#!/usr/bin/python3
"""
    This module contains the implementation of the sum function.
        :param a: an integer or a float
        :param b: an integer of a float
"""

def add_integer(a, b=98):
    """This function returns the sum of two integers
        :return: an integer
    """
    if isinstance(a, (list, dict, tuple)):
        raise TypeError("a must be an integer")
    if isinstance(b, (list, dict, tuple)):
        raise TypeError("b must be an integer")

    if not isinstance(a, (int, float)) or a == inf or a == -inf:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b == inf or b == -inf:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
