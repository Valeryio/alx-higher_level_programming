#!/usr/bin/python3
"""
    THis module contains a function that verify if an object is a from a class
    or of one of its subclasses
"""


def is_kind_of_class(obj, a_class):
    """
        This function verifies if an object of a subclass of a class
    Args:
        obj (object): the object to verify
        a_class (class): the class to use
    Return:
        True on SUCCESS
        False on FAILURE
    """
    if isinstance(obj, a_class):
        return True
    return False
