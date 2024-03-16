#!/usr/bin/python3

def max_integer(my_list=[]):
    """
        This function returns the max integer
        in the list

    Args:
        my_list: a list of integer

    Returns:
        A number on success, None otherwise
    """
    if len(my_list) == 0:
        return None

    max_int = my_list[0]

    for i in my_list:
        if (max_int < i):
            max_int = i

    return max_int
