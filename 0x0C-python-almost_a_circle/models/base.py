#!/usr/bin/python3
"""This module defines a Base class"""


import json
import turtle
from random import randint


class Base():
    """This is the base class with base functionalities
    All modules inherit from this class
    """
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
        shape = None
        if cls.__name__ == 'Rectangle':
            shape = cls(1, 1)
        if cls.__name__ == 'Square':
            shape = cls(1)
        shape.update(**dictionary)
        return shape

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
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
        except FileNotFoundError:
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
            list_dictionaries = []
            if list_objs:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(list_dictionaries))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the object to csv file
        The filename is <class name>.csv
        """
        obj_strs = None
        if cls.__name__ == 'Rectangle':
            obj_strs = map(lambda obj: '{:d},{:d},{:d},{:d},{:d}'.format(
                obj.id, obj.width, obj.height, obj.x, obj.y), list_objs)
        if cls.__name__ == 'Square':
            obj_strs = map(lambda obj: '{:d},{:d},{:d},{:d}'.format(
                obj.id, obj.size, obj.x, obj.y), list_objs)
        with open(cls.__name__+'.csv', 'w') as file:
            file.write('\n'.join(obj_strs)+'\n')

    @classmethod
    def load_from_file_csv(cls):
        """Read the object from csv file
        The filename is <class name>.csv
        """
        try:
            list_strs = []
            with open(cls.__name__+'.csv', 'r') as f:
                for line in f:
                    entry = line.strip()
                    list_strs.append(entry.split(','))
            obj_dicts = None
            if cls.__name__ == 'Rectangle':
                obj_dicts = map(lambda rect: {
                    'id': int(rect[0]),
                    'width': int(rect[1]),
                    'height': int(rect[2]),
                    'x': int(rect[3]),
                    'y': int(rect[4])
                    }, list_strs)
            if cls.__name__ == 'Square':
                obj_dicts = map(lambda rect: {
                    'id': int(rect[0]),
                    'size': int(rect[1]),
                    'x': int(rect[2]),
                    'y': int(rect[3])
                    }, list_strs)
            return [cls.create(**obj_dict) for obj_dict in obj_dicts]
        except (FileNotFoundError, TypeError, IndexError):
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws the objects using turtle"""
        brush = turtle.Turtle()
        brush.pensize(2)
        turtle.colormode(255)
        if list_rectangles is not None:
            for rect in list_rectangles:
                rect._draw(brush)
        if list_squares is not None:
            for rect in list_squares:
                rect._draw(brush)
        brush = turtle.done()

    def _draw(rect, brush):
        """This is a private method that does the actual drawing"""
        brush.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        fillcolor = (randint(0, 255), randint(0, 255), randint(0, 255))
        brush.fillcolor(*fillcolor)
        brush.penup()
        brush.goto(rect.x, rect.y)
        brush.begin_fill()
        brush.pendown()
        brush.forward(rect.width)
        brush.right(90)
        brush.forward(rect.height)
        brush.right(90)
        brush.forward(rect.width)
        brush.right(90)
        brush.forward(rect.height)
        brush.right(90)
        brush.end_fill()
