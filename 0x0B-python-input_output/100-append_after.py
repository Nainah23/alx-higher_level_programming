#!/usr/bin/python3
"""Defines a function that inserts into a txt file."""


def append_after(filename="", search_string="", new_string=""):
    """Append text to each line with a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The inserted string.
    """
    text = ""
    with open(filename) as x:
        for line in x:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as y:
        y.write(text)
