#!/usr/bin/python3
"""
    This module is used to deserialise classes
"""


def class_to_json(obj):
    """
        This function deserialise a class object
    Args:
        obj (object): the object to deserialize
    Return:
        A dict
    """
    return obj.__dict__
