#!/usr/bin/python3
"""a function that defines an object attribute lookup."""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return (dir(obj))
