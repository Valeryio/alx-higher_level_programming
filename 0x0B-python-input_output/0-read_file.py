#!/usr/bin/python3

def read_file(filename=""):
    """
        This function reads a file in format UTF-8
    Args:
        filename (string): the name of the file we want to open
    Returns:
        Nothing
    """

    with open(filename, encoding="UTF-8") as file:
        for line in file:
            print(line, end="")
