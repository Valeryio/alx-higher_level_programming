#!/usr/bin/python3
"""
    This module containes a function that write a file
"""


def write_file(filename="", text=""):
    """
        This function writes a file in format UTF-8
    Args:
        filename (string): the name of the file we want to open
        text (string): the text we want to write in the file
    Returns:
        Nothing
    """

    with open(filename, 'w', encoding="UTF-8") as file:
        nb = file.write(text)

    return nb
