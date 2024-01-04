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

    def area(self):
        """Gets Rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Gets rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    def __str__(self):
        """Prints the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")

            return ("".join(rect))

    def __repr__(self):
        """Gets the rectangle's string representation"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Returns a msg for every rectangle deleted"""
        print("Bye rectangle...")
