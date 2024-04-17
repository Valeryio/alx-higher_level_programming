#!/usr/bin/python3

"""
    This modules contains a function that verifies if a object is an
    instance of a class or of its subclasses
"""


def inherits_from(obj, a_class):
    """
        This function verifies if obj is an instance of a_class
        or from its subclasses
    Args:
        obj (object): the object to verify
        a_class (class): the class to use
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
