#!/usr/bin/python3
def safe_print_integer(value):
    """
        print safely an integer
    Args:
        @value: A value to print
    Return: A boolean
    """
    try:
        print("{:d}".format(int(value)))
    except:
        return False
    return True
