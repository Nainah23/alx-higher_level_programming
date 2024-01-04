#!/usr/bin/python3
"""Defines a rectangle"""

class Rectangle:
    """Defines as rectangle"""
    def __init__(self, width=0, height=0):
        """Rectangle initialization

        Args:
            width (int): Rectangle width(new)
            height (int): Rectangle height(new)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Define rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Define rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
