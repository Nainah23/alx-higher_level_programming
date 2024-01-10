#!/usr/bin/python3
"""Creates a class instance"""

class Student:
    """Defines a student"""
    
    def __init__(self, first_name, last_name, age):
        """Initializes new student
        Args:
            first_name (str): student first name
            last_name (str): student last name
            age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a student dict representation"""
        return self.__dict__
