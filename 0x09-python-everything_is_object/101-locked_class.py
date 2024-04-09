#!/usr/bin/python3
"""THis module contains a locked class that don't
    allow user to add dynamically attributes to the class
"""


class LockedClass:
    """This is a locked class"""
    __slots__ = ('first_name')
