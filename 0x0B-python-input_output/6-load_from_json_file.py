#!/usr/bin/python3
"""Defines a fn for reading JSON files"""
import json

def load_from_json(filename):
    """creates an Object from a JSON file"""
    with open(filename) as x:
        return json.load(x)
