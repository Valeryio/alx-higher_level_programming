#!/usr/bin/python3
"""
    Serialize an object and write into a file
"""
import json


def to_json_string(my_obj):
    """
        This function serialise an object
    Args:
        my_obj (string): The object to serialize
    Return: Nothing
    """
    return json.dumps(my_obj)
