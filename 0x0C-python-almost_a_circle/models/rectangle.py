#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """Representation of a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute in this order
        **kwargs are skipped if args exists and is not empty
        """
        my_attrs = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            setattr(self, my_attrs[i], arg)
        if not args:
            for name, value in kwargs.items():
                if name in my_attrs:
                    setattr(self, name, value)

    def display(self):
        """Displays the rectangle with '#' symbol"""
        rect = ['']*self.y + [' '*self.x + '#'*self.width]*self.height
        print('\n'.join(rect))

    def to_dictionary(self):
        """Returns a dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }

    def __str__(self):
        """Returns a string representation"""
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__validate_positive_integer('width', value)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__validate_positive_integer('height', value)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.__validate_zero_or_positive_integer('x', value)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.__validate_zero_or_positive_integer('y', value)
        self.__y = value

    def __validate_integer(self, attrname, value):
        """Validates that input is an integer"""
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(attrname))

    def __validate_positive_integer(self, attrname, value):
        """Validates that input is an integer and is > 0"""
        self.__validate_integer(attrname, value)
        if value <= 0:
            raise ValueError('{:s} must be > 0'.format(attrname))

    def __validate_zero_or_positive_integer(self, attrname, value):
        """Validates that input is an integer and is >= 0"""
        self.__validate_integer(attrname, value)
        if value < 0:
            raise ValueError('{:s} must be >= 0'.format(attrname))
