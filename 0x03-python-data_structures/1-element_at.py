#!/usr/bin/python3

def element_at(my_list, idx):
    """
        My search function

        Args:
            my_list: the list
            idx: the index of the searched element

        Returns:
            Returns the value at the index
    """
    if (idx < 0 or idx >= len(my_list)):
        return None

    return my_list[idx]
