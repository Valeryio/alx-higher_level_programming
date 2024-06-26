#!/usr/bin/python3

"""
    This module is a customised class of int
"""


class MyInt(int):
    """
        This is an extension of the class int
    Args:
        other (int): the integer to use
    Return:
        True on SUCCESS
        False on FAILURE
    """

    def __init__(self, value):
        super().__init__()

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)

    def __str__(self):
        return super().__str__()
