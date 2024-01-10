#!/usr/bin/python3
""" creating function """


class Student:
    """
    Defines a student with first_name, last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings
                          If None, retrieve all attributes.

        Returns:
            dict: A dictionary
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {attr: getattr(self, attr, None) for attr in attrs}

    def reload_from_json(self, json_data):
        """
        Replaces all attributes of the Student instance based on a dictionary.

        Args:
            json_data (dict): A dictionary
        """
        for key, value in json_data.items():
            setattr(self, key, value)
