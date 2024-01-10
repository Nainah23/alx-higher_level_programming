#!/usr/bin/python3
"""Defines a fn that appends a file"""
def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)

    Args:
        filename (str): file to append to
        text (str): string to add to the file
    Return:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as x:
        return x.write(text)
