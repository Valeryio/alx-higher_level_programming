#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
        This function delete an element

    Args:
        my_lists: the list of numbers
        idx: the index

    Returns:
        A new list
    """
    new_list = []
    my_list.pop(idx)
    new_list = my_list

    return new_list
