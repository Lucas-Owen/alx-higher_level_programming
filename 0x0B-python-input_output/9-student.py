#!/usr/bin/python3
"""This module defines a Student class"""


class Student():
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of a student instance"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
