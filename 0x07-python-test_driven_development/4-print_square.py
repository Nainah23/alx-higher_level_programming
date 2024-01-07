#!/usr/bin/python3
"""Define a fn that will print a square"""
def print_square(size):
    """prints a square using #
    Args:
        size (int). square width/height
    Raises:
        TypeError: if size != int
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        [print ("#", end="") for y in range(size)]
        print("")
