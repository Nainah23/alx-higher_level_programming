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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
