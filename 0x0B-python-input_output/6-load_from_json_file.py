#!/usr/bin/python3
"""
    THis module deserialize an object in json and save it into a file
"""
import json


def load_from_json_file(filename):
    """
        This function deserialize a python's object to a file
    Args:
        my_obj (object): the object to deserialize
        filename (string): The file's name
    """
    with open(filename, 'r', encoding="UTF-8") as json_file:
        return json.load(json_file)
