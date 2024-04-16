#!/usr/bin/python3
"""
    This module deserialise a json string
"""
import json


def from_json_string(my_str):
    """
        This function return a json string
    Args:
        @my_str: (string), the string to use
    Return:
        A string
    """
    return json.loads(my_str)
