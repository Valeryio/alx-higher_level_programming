#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
        This function creates a set of all elements present in
        only one set.
    Args:
        set_1: the first set
        set_2: the second set
    Returns:
        A set
    """

    new_set = set_1 | set_2

    for i in range(len(new_set)):
        if list(new_set)[i] in set_1 and list(new_set)[i] in set_2:
            new_set.remove(list(new_set)[i])

    return new_set
