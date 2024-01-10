#!/usr/bin/python3
"""Defines a fn that writes a file"""
def write_file(filename="", text=""):
    """
    Write a function that writes a string to a text file (UTF8)
    Args:
        filename (str): file to be written
        text (str): text to write to filename
    Return:
        No. of characters written
    """
    with open(filename, "w", encoding="utf-8") as x:
        return x.write(text)
