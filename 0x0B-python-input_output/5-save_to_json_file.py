#!/usr/bin/python3
"""Define a fn that writes JSON to a file"""
import json

def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation:"""
    with open(filename, "w") as x:
        json.dump(my_obj, x)
