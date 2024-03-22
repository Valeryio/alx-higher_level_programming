#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
        This function deletes an element by its key
    Args:
        @a_dictionary: The dictionary of elements
        @key: the key used to identity the element
    Returns:
        A dict
    """
    if key in a_dictionary.keys():
        a_dictionary.pop(key)

    return a_dictionary
