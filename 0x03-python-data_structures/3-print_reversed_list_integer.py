#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
        My reversed print function

        Args:
            my_list: a list
    """
    if my_list is None:
        print("".format(), end='')
    else:
        my_list.reverse()

        for i in my_list:
            print("{:d}".format(i))
