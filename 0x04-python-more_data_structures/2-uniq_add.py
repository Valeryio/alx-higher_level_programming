#!/usr/bin/python

def uniq_add(my_list = []):
    """
        This function adds unique integers
        in a list
    Args:
        my_list: the list of integes
    Returns:
        An integer
    """
    return sum(set(my_list))
