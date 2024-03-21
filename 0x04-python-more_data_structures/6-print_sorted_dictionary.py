#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
        This function sorts a dictionary
    Args:
        A dictionnary
    Returns:
        Nothing
    """

    sorted_list = sorted(list(a_dictionary.keys()))

    for i in sorted_list:
        print("{}: {}".format(i, a_dictionary[i]))
