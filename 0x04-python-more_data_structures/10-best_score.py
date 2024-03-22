#!/usr/bin/python3

def best_score(a_dictionary):
    """
        Look for the biggest integer value in a dic
    Args:
        @a_dictionary: a dict
    Returns:
        A string
    """

    if a_dictionary is None:
        return None

#    max_key = max(a_dictionary.values())
    best_key = ""

    for key, value in a_dictionary.items():
        if value == max(a_dictionary.values()):
            best_key = key

    return best_key
