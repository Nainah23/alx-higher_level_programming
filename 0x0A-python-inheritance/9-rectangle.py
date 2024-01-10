#!/usr/bin/python3
"""Represents a class Rectangle inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle by BaseGeometry"""
    def __init__(self, width, height):
        """New Rectangle initialization.

        Args:
            width (int): New Rectangle width.
            height (int): New Rectangle height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Return the Rectangle str and print representation."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
