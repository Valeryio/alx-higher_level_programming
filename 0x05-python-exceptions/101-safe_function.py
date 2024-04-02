#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
        This function executes safely another one
    Args:
        @fct: The function to execute
        @args: its arguments
    Return:
        A result or None
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
