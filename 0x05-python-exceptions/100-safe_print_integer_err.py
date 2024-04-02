#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
        print safely an integer
    Args:
        @value: A value to print
    Return: A boolean
    """
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: {}".format(e))
        return False
    return True
