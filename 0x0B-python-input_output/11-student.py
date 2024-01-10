#!/usr/bin/python3
"""Creates a class Student."""


class Student:
    """Student representation"""

    def __init__(self, first_name, last_name, age):
        """new Student Initialization.

        Args:
            first_name (str): The student first name
            last_name (str): The student last name
            age (int): The student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Obtain a dictionary representation of the Student.

        If attrs is a list of strings, include only the attributes specified in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
