#!/usr/bin/python3
"""Defines a MyInt class inheriting from an integer."""


class MyInt(int):
    """Reverse int operators == and !=."""

    def __eq__(self, value):
        """It overrides == operator with !=."""
        return self.real != value

    def __ne__(self, value):
        """It overrides != operator with ==."""
        return self.real == value
