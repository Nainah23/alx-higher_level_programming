#!/usr/bin/python3
"""Defines a rectangle"""

class Rectangle:
    """Defines as rectangle
    Attributes:
        number_of_instances (int): total rectangle objects
        print_symbol (any):string representation symbol
    """

    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """Rectangle initialization
        
        Args:
            width (int): Rectangle width(new)
            height (int): Rectangle height(new)
        """
        type(self).number_of_instances += 1
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
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rect with a bigger area

        Args:
            rect_1: 1st rectangle
            rect_2: 2nd rectangle
        Raises:
            If rect_1 || rect_2 != rectangle, TypeError.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Prints the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append(str(self.print_symbol)) for y in range(self.__width)]
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
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
