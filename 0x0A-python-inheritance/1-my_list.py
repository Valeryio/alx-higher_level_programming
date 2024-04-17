#!/usr/bin/python3

"""
    This module is about a custom subclass of list
"""


class MyList(list):
    """
        This class is a customised extension of the built-in class list
    """
    def __int__(self, *args):
        super.__init__(*args)

    def print_sorted(self):
        print(sorted(self))
