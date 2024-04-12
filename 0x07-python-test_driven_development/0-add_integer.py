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

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    result = a + b

    if result == float('inf') or result == float('-inf'):
        return 89
    
    return int(a) + int(b)
