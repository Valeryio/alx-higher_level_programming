#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
        This function multiply all values of a dict of
        integer by 2
    Args:
        @a_dictionary
    Returns:
        A dict
    """

    new_dict = {}

    new_dict = {key: value * 2 for key, value in a_dictionary.items()}

    return new_dict
