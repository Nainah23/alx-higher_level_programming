#!/usr/bin/python3
"""Defines a fn that prints my name"""
def say_my_name(first_name, last_name=""):
    """Prints my name

    Args:
        first_name (str): first name
        last_name (str): last name
        Raises:
            TypeError: if either names is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
