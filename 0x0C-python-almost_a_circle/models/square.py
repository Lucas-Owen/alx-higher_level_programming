#!/usr/bin/python3
"""This module defines a square class that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute in this order"""
        my_attrs = ['id', 'size', 'x', 'y']
        for i, arg in enumerate(args):
            setattr(self, my_attrs[i], arg)
        if not args:
            for name, value in kwargs.items():
                if name in my_attrs:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Returns a dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }

    def __str__(self):
        """Returns a string representation"""
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value
