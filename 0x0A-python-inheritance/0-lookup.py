#!/usr/bin/python3
"""
    This module contains a function that list attributes and methods of
    classes
"""


def lookup(obj):
    """
        This function returns all the methods and the attributes of a
        class object
    Args:
        obj (class): An instance of an user-defined class
    Returns:
        A list
    """
    return obj.__dict__
