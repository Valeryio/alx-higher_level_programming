#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(10, 2, 2, 9, 12)

    def test_init(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)

        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r2.y, 9)

    def test_setter(self):
        with self.assertRaises(ValueError):
            r4 = Rectangle(0, 1)
            r4 = Rectangle(1, 0)
            r4 = Rectangle(1, 2, -1)
            r4 = Rectangle(1, 2, 3, -1)

        with self.assertRaises(TypeError):
            r5 = Rectangle('a', 1)
            r5 = Rectangle(1, 'a')
            r5 = Rectangle(1, 2, 'a')
            r5 = Rectangle(1, 2, 3, 'a')

    def test_area(self):
        r4 = Rectangle(8, 7)

        self.assertEqual(r4.area(), 56)
