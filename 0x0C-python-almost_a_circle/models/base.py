#!/usr/bin/python3
"""This module defines a Base class"""


import json


class Base():
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the instance with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Returns a class instance from dictionary"""
        shape = cls(1, 1)
        shape.update(**dictionary)
        return shape

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns python list from json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Loads and returns a list of instances from file
        The filename is <class name>.json
        """
        try:
            list_dictionaries = []
            with open(cls.__name__+'.json', 'r') as f:
                list_dictionaries = cls.from_json_string(f.read())
            return [cls.create(**obj) for obj in list_dictionaries]
        except (FileExistsError, FileNotFoundError):
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        The filename is <class name>.json
        Args:
            cls <class>:
            list_objs: List of objects that inherit from Base
        """
        with open(cls.__name__ + '.json', 'w') as file:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(list_dictionaries))
