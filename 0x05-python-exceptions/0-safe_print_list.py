#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
        Print safely a list

    Args:
        @mylist: The list to print
        @x: the number to use
    Return: An integer
    """
    j = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            j += 1
        except IndexError:
            break
    print("")
    return j
