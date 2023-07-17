#!/usr/bin/python3
"""This module defines a unittest for Square class"""


from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import random
from ..models.square import Square


class TestSquare(TestCase):
    """This class tests the different functionalities of models.Base"""
    def test_init(self):
        """Tests the creation of a Square"""
        r1 = Square(10)
        self.assertEqual(0, r1.id)
        self.assertEqual(10, r1.width)
        self.assertEqual(10, r1.height)
        self.assertEqual(10, r1.size)
        self.assertEqual(0, r1.x)
        self.assertEqual(0, r1.y)

        r2 = Square(2)
        self.assertEqual(2, r2.id)
        self.assertEqual(2, r2.width)
        self.assertEqual(2, r2.height)
        self.assertEqual(2, r1.size)
        self.assertEqual(0, r2.x)
        self.assertEqual(0, r2.y)

        r3 = Square(10, 2, 4, 12)
        self.assertEqual(12, r3.id)
        self.assertEqual(10, r3.width)
        self.assertEqual(10, r3.height)
        self.assertEqual(10, r1.size)
        self.assertEqual(2, r3.x)
        self.assertEqual(4, r3.y)

        self.assertRaises(TypeError, Square, '10')
        self.assertRaises(TypeError, Square, 10, '1', 0)
        self.assertRaises(TypeError, Square, 10, 1, '0')

        self.assertRaises(ValueError, Square, 0, 1, 0)
        self.assertRaises(ValueError, Square, 1, -1, 0)
        self.assertRaises(ValueError, Square, 1, 1, -1)

    def test_area(self):
        """Tests for area method"""
        for i in range(0, 10):
            size = random.randint(1)
            sq = Square(size)
            self.assertEqual(size * size, sq.area())

    def test_display(self):
        """Tests for the display method"""
        with patch('sys.stdout', new = StringIO()) as output:
            expected = '####\n####\n####\n####\n'
            Square(4).display()
            self.assertEqual(expected, output.getValue())
        with patch('sys.stdout', new = StringIO()) as output:
            expected = '\n\n  ##\n  ##\n'
            Square(2, 2, 2).display()
            self.assertEqual(expected, output.getValue())

    def test_str(self):
        """Tests for the __str__ function"""
        r1 = Square(4, 2, 1, 12)
        r2 = Square(5, 1)
        self.assertEqual(str(r1), '[Square] (12) 2/1 - 4')
        self.assertEqual(str(r2), '[Square] (1) 1/0 - 5')

    def test_update(self):
        """Tests for the update function"""
        r1 = Square(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(89, r1.id)
        self.assertEqual(10, r1.size)
        self.assertEqual(10, r1.width)
        self.assertEqual(10, r1.height)
        self.assertEqual(10, r1.x)
        self.assertEqual(10, r1.y)

        r1.update(89, 2)
        self.assertEqual(89, r1.id)
        self.assertEqual(2, r1.size)
        self.assertEqual(2, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(10, r1.x)
        self.assertEqual(10, r1.y)

        r1.update(89, 2, 4)
        self.assertEqual(89, r1.id)
        self.assertEqual(2, r1.size)
        self.assertEqual(2, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(4, r1.x)
        self.assertEqual(10, r1.y)

        r1.update(89, 2, 4, 5)
        self.assertEqual(89, r1.id)
        self.assertEqual(2, r1.size)
        self.assertEqual(2, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(4, r1.x)
        self.assertEqual(5, r1.y)

        r2 = Square(10, 10, 10, 10, 1)
        r2.update(size=4)
        self.assertEqual(10, r2.id)
        self.assertEqual(4, r1.size)
        self.assertEqual(4, r2.width)
        self.assertEqual(4, r2.height)
        self.assertEqual(10, r2.x)
        self.assertEqual(10, r2.y)

        r2.update(height=1)
        self.assertEqual(10, r2.id)
        self.assertEqual(1, r1.size)
        self.assertEqual(1, r2.width)
        self.assertEqual(1, r2.height)
        self.assertEqual(10, r2.x)
        self.assertEqual(10, r2.y)

        r2.update(width=2, x=2)
        self.assertEqual(10, r2.id)
        self.assertEqual(2, r1.size)
        self.assertEqual(2, r2.width)
        self.assertEqual(2, r2.height)
        self.assertEqual(2, r2.x)
        self.assertEqual(10, r2.y)

        r2.update(y=1, width=1, x=3, id=89)
        self.assertEqual(89, r2.id)
        self.assertEqual(1, r1.size)
        self.assertEqual(1, r2.width)
        self.assertEqual(1, r2.height)
        self.assertEqual(3, r2.x)
        self.assertEqual(1, r2.y)

        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(89, r2.id)
        self.assertEqual(2, r1.size)
        self.assertEqual(2, r2.width)
        self.assertEqual(2, r2.height)
        self.assertEqual(1, r2.x)
        self.assertEqual(3, r2.y)
