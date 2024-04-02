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
    c = 0

    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        print("Inside result: {}".format(c))
        return c
