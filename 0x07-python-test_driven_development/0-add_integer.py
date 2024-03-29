#!/usr/bin/python3
"""Defines an add fn for intergers"""
def add_integer(a, b=98):
    """Adds a and b
    if a float, convert first to int
    Raise:
    TypeError if not an integer
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
