#!/usr/bin/python3
"""Represents a fn adding attributes to instances"""

def add_attribute(obj, att, value):
    """
    If possible, it add a new attribute to an instances

    Args:
        obj (any): The object to be added an attribute to.
        att (str): The attribute name to add to obj.
        value (any): The att value.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
