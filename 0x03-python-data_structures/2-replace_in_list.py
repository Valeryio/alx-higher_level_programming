#!/usr/bin/python3

def element_at(my_list, idx, element):
    """
        A function that replaces an element

        Args:
            my_list: the list
            idx: the index of the searched element
            element: the element to replace

        Returns:
            Returns the value at the index
    """
    if (idx < 0 or idx >= len(my_list)):
        return my_list

    my_list[idx] = element

    return my_list
