#!/usr/bin/python3
"""
    This is the module of the BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        This is the Rectangle class
    Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
