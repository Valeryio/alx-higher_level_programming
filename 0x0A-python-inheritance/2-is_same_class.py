#!/usr/bin/python3

"""
    This module contains one only verification function
"""


def is_same_class(obj, a_class):
    """
        This function verifies if obj is an instance of a_class
    Args:
        obj (object): the object to use
        a_class (class): the class to use
    Return:
        True on SUCCESS
        False on FAILURE
    """
    if type(obj) is a_class:
        return True
    return False
