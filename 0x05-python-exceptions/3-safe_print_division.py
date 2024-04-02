#!/usr/bin/python3

def safe_print_division(a, b):
    """
        Make a safe division
    Args:
        a: the dividend
        b: the divisor
    Return:
        A number or None
    """

    try:
        c = a / b
        print("Inside result: {}".format(c))
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return None
