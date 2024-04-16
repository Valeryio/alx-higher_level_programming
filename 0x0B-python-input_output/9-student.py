#!/usr/bin/python3
"""
    This module contain a class
"""


class Student:
    """
        This is the implementation of the class Student

        Attributes:
            age (int): the age of the student
            last_name (str): the last_name of the student
            first_name (str): the first name of the student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
