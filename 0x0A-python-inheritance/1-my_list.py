#!/usr/bin/python3
"""Represents class MyList from an inherited list"""

class MyList(list):
    """ inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
