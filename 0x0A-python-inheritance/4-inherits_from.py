#!/usr/bin/python3
"""Introduces a class and a function for checking if an object is an inherited instance of a specific class."""

def inherits_from(obj, a_class):
    """
    Verifies whether obj is an  inherited instance of a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj.

    Returns:
        True if obj is an inherited instance of a_class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
