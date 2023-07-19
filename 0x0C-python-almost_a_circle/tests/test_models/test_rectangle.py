#!/usr/bin/python3
"""This module defines a unittest for Rectangle class"""


from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import random
from models.rectangle import Rectangle


class TestRectangle(TestCase):
    """This class tests the different functionalities of models.Base"""
    def test_init_normal(self):
        """Tests the creation of a rectangle"""
        rect1 = Rectangle(10, 2)
        self.assertEqual(10, rect1.width)
        self.assertEqual(2, rect1.height)
        self.assertEqual(0, rect1.x)
        self.assertEqual(0, rect1.y)

        rect2 = Rectangle(2, 10)
        self.assertEqual(2, rect2.width)
        self.assertEqual(10, rect2.height)
        self.assertEqual(0, rect2.x)
        self.assertEqual(0, rect2.y)

        self.assertEqual(1, rect2.id - rect1.id)

        rect3 = Rectangle(10, 2, 2, 4, 12)
        self.assertEqual(12, rect3.id)
        self.assertEqual(10, rect3.width)
        self.assertEqual(2, rect3.height)
        self.assertEqual(2, rect3.x)
        self.assertEqual(4, rect3.y)

    def test_init_error(self):
        """Tests for trying to initialize with invalid input"""
        self.assertRaises(TypeError, Rectangle, '10', 2)
        self.assertRaises(TypeError, Rectangle, 10, '2')
        self.assertRaises(TypeError, Rectangle, 10, 2, '1', 0)
        self.assertRaises(TypeError, Rectangle, 10, 2, 1, '0')

        self.assertRaises(ValueError, Rectangle, 0, '2', 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 0, 1, 0)
        self.assertRaises(ValueError, Rectangle, -1, '2', 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, -1, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 1, -1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1)

    def test_area(self):
        """Tests for area method"""
        for i in range(0, 10):
            width = random.randint(1, 100)
            height = random.randint(1, 100)
            rect = Rectangle(width, height)
            self.assertEqual(width * height, rect.area())

    def test_display_without_xy(self):
        """Tests for the display method"""
        with patch('sys.stdout', new=StringIO()) as output:
            expected = '####\n####\n####\n####\n####\n####\n'
            Rectangle(4, 6).display()
            self.assertEqual(expected, output.getvalue())

    def test_display_with_xy(self):
        """Tests for displaying with coordinates set"""
        with patch('sys.stdout', new=StringIO()) as output:
            expected = '\n\n  ##\n  ##\n  ##\n'
            Rectangle(2, 3, 2, 2).display()
            self.assertEqual(expected, output.getvalue())

    def test_to_dictionary(self):
        """Tests the to_dictionary method"""
        r_dict = Rectangle(10, 2, 1, 9, 1).to_dictionary()
        self.assertTrue(type(r_dict) is dict)
        self.assertEqual({'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10},
                         r_dict)

    def test_str(self):
        """Tests for the __str__ function"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1, id=1)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')
        self.assertEqual(str(r2), '[Rectangle] (1) 1/0 - 5/5')

    def test_update_args(self):
        """Tests for the update function"""
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)
        self.assertEqual(89, rect.id)
        self.assertEqual(10, rect.width)
        self.assertEqual(10, rect.height)
        self.assertEqual(10, rect.x)
        self.assertEqual(10, rect.y)

        rect.update(89, 2)
        self.assertEqual(89, rect.id)
        self.assertEqual(2, rect.width)
        self.assertEqual(10, rect.height)
        self.assertEqual(10, rect.x)
        self.assertEqual(10, rect.y)

        rect.update(89, 2, 3)
        self.assertEqual(89, rect.id)
        self.assertEqual(2, rect.width)
        self.assertEqual(3, rect.height)
        self.assertEqual(10, rect.x)
        self.assertEqual(10, rect.y)

        rect.update(89, 2, 3, 4)
        self.assertEqual(89, rect.id)
        self.assertEqual(2, rect.width)
        self.assertEqual(3, rect.height)
        self.assertEqual(4, rect.x)
        self.assertEqual(10, rect.y)

        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(89, rect.id)
        self.assertEqual(2, rect.width)
        self.assertEqual(3, rect.height)
        self.assertEqual(4, rect.x)
        self.assertEqual(5, rect.y)

    def test_update_kwargs(self):
        """Tests for update with kwargs"""
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(height=1)
        self.assertEqual(10, rect.id)
        self.assertEqual(10, rect.width)
        self.assertEqual(1, rect.height)
        self.assertEqual(10, rect.x)
        self.assertEqual(10, rect.y)

        rect.update(width=1, x=2)
        self.assertEqual(10, rect.id)
        self.assertEqual(1, rect.width)
        self.assertEqual(1, rect.height)
        self.assertEqual(2, rect.x)
        self.assertEqual(10, rect.y)

        rect.update(y=1, width=2, x=3, id=89)
        self.assertEqual(89, rect.id)
        self.assertEqual(2, rect.width)
        self.assertEqual(1, rect.height)
        self.assertEqual(3, rect.x)
        self.assertEqual(1, rect.y)

        rect.update(x=1, height=2, y=3, width=4)
        self.assertEqual(89, rect.id)
        self.assertEqual(4, rect.width)
        self.assertEqual(2, rect.height)
        self.assertEqual(1, rect.x)
        self.assertEqual(3, rect.y)

    def test_update_args_kwargs(self):
        """Tests for update with both arg and kwargs"""
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(10, 9, 8, height=4, x=2, y=1)
        self.assertEqual(10, rect.id)
        self.assertEqual(9, rect.width)
        self.assertEqual(8, rect.height)
        self.assertEqual(10, rect.x)
        self.assertEqual(10, rect.y)

    def test_create(self):
        """Tests for the create classmethod in Base"""
        rect = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(rect.id, 89)
        rect = Rectangle.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(89, rect.id)
        self.assertEqual(1, rect.width)
        rect = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(89, rect.id)
        self.assertEqual(1, rect.width)
        self.assertEqual(2, rect.height)
        rect = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(89, rect.id)
        self.assertEqual(1, rect.width)
        self.assertEqual(2, rect.height)
        self.assertEqual(3, rect.x)
        rect = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(89, rect.id)
        self.assertEqual(1, rect.width)
        self.assertEqual(2, rect.height)
        self.assertEqual(3, rect.x)
        self.assertEqual(4, rect.y)
