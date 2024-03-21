#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
        This function replace search in my_list
        by replace
    Args:
        my_list: the list
        search: the element you searched
        replace: the element used to replace
    Returns:
        The list
    """

    newlist = []

    for i in range(len(my_list)):
        if my_list[i] == search:
            newlist.append(replace)
        else:
            newlist.append(my_list[i])

    return newlist
