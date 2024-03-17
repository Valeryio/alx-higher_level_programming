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
    to_delete = 0

    for i in my_list:
        if i == my_list[idx]:
            to_delete = i

    my_list.remove(to_delete)
    new_list = my_list

    return new_list
