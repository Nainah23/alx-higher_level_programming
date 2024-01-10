#!/usr/bin/python3
"""Defines BaseGeometry of the base geometry class."""


class BaseGeometry:
    """Stands for base geometry."""

    def area(self):
        """! implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Will validate parameter as int

        Args:
            name (str): The parameter name.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
