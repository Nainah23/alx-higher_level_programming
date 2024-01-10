#!/usr/bin/python3
"""Introduces a class and a function for checking if an object is an instance or an inherited instance of a specific class."""

def is_kind_of_class(obj, a_class):
    """
    Verifies whether obj is an instance or inherited instance of a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj.

    Returns:
        True if obj is an instance or inherited instance of a_class, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
