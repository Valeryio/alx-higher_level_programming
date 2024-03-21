#!/usr/bin/python

def uniq_add(my_list=[]):
    """
        This function adds unique integers
        in a list
    Args:
        my_list: the list of integes
    Result:
        An integer
    """

    new_list = []

    for i in range(len(my_list)):
        if my_list[i] in new_list:
            continue
        else:
            new_list.append(my_list[i])

    return sum(new_list)
