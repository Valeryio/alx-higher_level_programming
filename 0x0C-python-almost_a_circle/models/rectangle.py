#!/usr/bin/python3
"""
    This module contains a simple class that inherits from the base
    class. Here we have a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
        This class is the implementation of a rectangle
    Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        x (int): the absisse of the rectangle
        y (int): the ordinate of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# Getter and setter for the attribute : width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.typevalidator("width", width)

        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

# Getter and setter for the attribute : height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.typevalidator("height", height)

        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

# Getter and setter for the attribute : x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.typevalidator("x", x)

        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

# Getter and setter for the attribute : y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.typevalidator("y", y)

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

# Validator method
    def typevalidator(self, attribute, value):
        """
            This function is a validator to ensure that we get the right
            type for the attributes of our object
        Args:
            attribute (string): the name of the attribute
            value (int): the value of the attribute
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
