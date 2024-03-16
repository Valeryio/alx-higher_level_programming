#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
        My print function

        Args:
            my_list: a list
    """
    try:
        int(my_list)
    except TypeError:
        pass

    for i in my_list:
        print("{a}".format(a=i))
