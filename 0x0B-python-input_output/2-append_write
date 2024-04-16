#!/usr/bin/python3
"""
    This module containes a function that append a file
"""


def append_write(filename="", text=""):
    """
        This function append to a file a string a file in format UTF-8
    Args:
        filename (string): the name of the file we want to open
        text (string): the text we want to write in the file
    Returns:
        Nothing
    """

    with open(filename, 'a', encoding="UTF-8") as file:
        nb = file.write(text)

    return nb
