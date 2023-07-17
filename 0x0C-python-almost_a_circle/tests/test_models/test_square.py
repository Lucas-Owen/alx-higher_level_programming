#!/usr/bin/python3
"""This module defines a unittest for Square class"""


from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import random
from models.square import Square


class TestSquare(TestCase):
    """This class tests the different functionalities of models.Base"""
    def test_init_normal(self):
        """Tests the creation of a Square"""
        sq1 = Square(10)
        self.assertEqual(10, sq1.size)
        self.assertEqual(10, sq1.width)
        self.assertEqual(10, sq1.height)
        self.assertEqual(0, sq1.x)
        self.assertEqual(0, sq1.y)

        sq2 = Square(2)
        self.assertEqual(2, sq2.size)
        self.assertEqual(2, sq2.width)
        self.assertEqual(2, sq2.height)
        self.assertEqual(0, sq2.x)
        self.assertEqual(0, sq2.y)

        self.assertEqual(1, sq2.id - sq1.id)

        sq3 = Square(10, 2, 4, 12)
        self.assertEqual(12, sq3.id)
        self.assertEqual(10, sq3.size)
        self.assertEqual(10, sq3.width)
        self.assertEqual(10, sq3.height)
        self.assertEqual(2, sq3.x)
        self.assertEqual(4, sq3.y)

    def test_init_error(self):
        """Tests for trying to initialize with invalid input"""
        self.assertRaises(TypeError, Square, '10')
        self.assertRaises(TypeError, Square, 10, '1', 0)
        self.assertRaises(TypeError, Square, 2, 1, '0')

        self.assertRaises(ValueError, Square, 0, 1, 0)
        self.assertRaises(ValueError, Square, 1, -1, 0)
        self.assertRaises(ValueError, Square, 1, 1, -1)

    def test_area(self):
        """Tests for area method"""
        for i in range(0, 10):
            size = random.randint(1, 100)
            square = Square(size)
            self.assertEqual(size * size, square.area())

    def test_display_without_xy(self):
        """Tests for the display method"""
        with patch('sys.stdout', new = StringIO()) as output:
            expected = '####\n####\n####\n####\n'
            Square(4).display()
            self.assertEqual(expected, output.getvalue())

    def test_display_with_xy(self):
        """Tests for displaying with coordinates set"""
        with patch('sys.stdout', new = StringIO()) as output:
            expected = '\n\n  ##\n  ##\n'
            Square(2, 2, 2).display()
            self.assertEqual(expected, output.getvalue())

    def test_str(self):
        """Tests for the __str__ function"""
        r1 = Square(4, 2, 1, 12)
        r2 = Square(5, 1, id=1)
        self.assertEqual(str(r1), '[Square] (12) 2/1 - 4')
        self.assertEqual(str(r2), '[Square] (1) 1/0 - 5')

    def test_update_args(self):
        """Tests for the update function"""
        sqr = Square(10, 10, 10, 10)
        sqr.update(89)
        self.assertEqual(89, sqr.id)
        self.assertEqual(10, sqr.size)
        self.assertEqual(10, sqr.width)
        self.assertEqual(10, sqr.height)
        self.assertEqual(10, sqr.x)
        self.assertEqual(10, sqr.y)

        sqr.update(89, 2)
        self.assertEqual(89, sqr.id)
        self.assertEqual(2, sqr.size)
        self.assertEqual(2, sqr.width)
        self.assertEqual(2, sqr.height)
        self.assertEqual(10, sqr.x)
        self.assertEqual(10, sqr.y)

        sqr.update(89, 2)
        self.assertEqual(89, sqr.id)
        self.assertEqual(2, sqr.size)
        self.assertEqual(2, sqr.width)
        self.assertEqual(2, sqr.height)
        self.assertEqual(10, sqr.x)
        self.assertEqual(10, sqr.y)

        sqr.update(89, 2, 4)
        self.assertEqual(89, sqr.id)
        self.assertEqual(2, sqr.size)
        self.assertEqual(2, sqr.width)
        self.assertEqual(2, sqr.height)
        self.assertEqual(4, sqr.x)
        self.assertEqual(10, sqr.y)

        sqr.update(89, 2, 4, 5)
        self.assertEqual(89, sqr.id)
        self.assertEqual(2, sqr.size)
        self.assertEqual(2, sqr.width)
        self.assertEqual(2, sqr.height)
        self.assertEqual(4, sqr.x)
        self.assertEqual(5, sqr.y)

    def test_update_kwargs(self):
        """Tests for update with kwargs"""
        sqr = Square(10, 10, 10, 10)
        sqr.update(height=1, width=4)
        self.assertEqual(10, sqr.id)
        self.assertEqual(10, sqr.size)
        self.assertEqual(10, sqr.width)
        self.assertEqual(10, sqr.height)
        self.assertEqual(10, sqr.x)
        self.assertEqual(10, sqr.y)

        sqr.update(size=1, x=2)
        self.assertEqual(10, sqr.id)
        self.assertEqual(1, sqr.size)
        self.assertEqual(1, sqr.width)
        self.assertEqual(1, sqr.height)
        self.assertEqual(2, sqr.x)
        self.assertEqual(10, sqr.y)

        sqr.update(y=1, size=2, x=3, id=89)
        self.assertEqual(89, sqr.id)
        self.assertEqual(2, sqr.size)
        self.assertEqual(2, sqr.width)
        self.assertEqual(2, sqr.height)
        self.assertEqual(3, sqr.x)
        self.assertEqual(1, sqr.y)

        sqr.update(x=1, height=2, y=3, size=4)
        self.assertEqual(89, sqr.id)
        self.assertEqual(4, sqr.size)
        self.assertEqual(4, sqr.width)
        self.assertEqual(4, sqr.height)
        self.assertEqual(1, sqr.x)
        self.assertEqual(3, sqr.y)

    def test_update_args_kwargs(self):
        """Tests for update with both arg and kwargs"""
        sqr = Square(10, 10, 10, 10)
        sqr.update(10, 9, height=4, x=2, y=1)
        self.assertEqual(10, sqr.id)
        self.assertEqual(9, sqr.size)
        self.assertEqual(9, sqr.width)
        self.assertEqual(9, sqr.height)
        self.assertEqual(10, sqr.x)
        self.assertEqual(10, sqr.y)
