#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
        This function updates a dictionary
    Args:
        @a_dictionary: the dictionary to update
        @key: the key to use
        @value: the value to change
    Results:
        A dictionary
    """

    a_dictionary.update({key: value})

    return a_dictionary
