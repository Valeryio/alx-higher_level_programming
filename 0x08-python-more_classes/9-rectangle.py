#!/usr/bin/python3
"""
    This module is about a class that we created to manipulate rectangles
"""


class Rectangle:
    """This is an empty class of rectangle

        Note:
        Args:
        Attributes:
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        representation = ''
        if self.width == 0 or self.height == 0:
            return ''

        for i in range(self.height):
            for j in range(self.width):
                representation += str(self.print_symbol)
            if i < (self.height - 1):
                representation += '\n'
        return representation

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        if type(self).number_of_instances <= 0:
            type(self).number_of_instances = 0
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """ This function return the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def area(self):
        """ This function return the area of a rectangle
        """
        return self.__width * self.__height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
