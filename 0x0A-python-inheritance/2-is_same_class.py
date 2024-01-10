#!/usr/bin/python3
"""Defines a fn that checks class"""

def is_same_class(obj, a_class):
    """Check if an object is particularly from a specific class

    Args:
        obj (any): object to be checked.
        a_class (type): The class to where the obj type is to be matched
    Returns:
        True if the object is exactly an instance of the specified class ; otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
