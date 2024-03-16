#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
        Modify and creates the copy of a new
        function

        Args:
            my_list a list
            idx an element
            element an element

        Returns: 
            A new list data stucture
    """

    if (idx < 0 or idx <= len(my_list)):
        return my_list

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
