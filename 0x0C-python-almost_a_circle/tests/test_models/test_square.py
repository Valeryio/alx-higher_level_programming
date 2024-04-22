#!/usr/bin/python3

"""
    This is a square module testing
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.s1 = Square(5)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)

    def test_print(self):
        result1 = "[Square] (1) 0/0 - 5"
        self.assertEqual(print(self.s1), result1)
