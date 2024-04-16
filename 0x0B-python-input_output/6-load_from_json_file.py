#!/usr/bin/python3
"""
    THis module serialize an object in json and save it into a file
"""
import json


def load_from_json_file(my_obj, filename):
    """
        This function serialize a python's object to a file
    Args:
        my_obj (object): the object to serialize
        filename (string): The file's name
    """
    with open(filename, 'w', encoding="UTF-8") as json_file:
        json.load(my_obj, json_file)
