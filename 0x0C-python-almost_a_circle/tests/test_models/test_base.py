#!/usr/bin/python3
"""This module defines a unittest for base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """This class tests the different functionalities of models.Base"""
    def test_create(self):
        """Tests the Base constructor"""
        b1 = Base()
        self.assertEqual(1, b1.id)
        b2 = Base()
        self.assertEqual(2, b2.id)
        b3 = Base()
        self.assertEqual(3, b3.id)
        b4 = Base(12)
        self.assertEqual(12, b4.id)
        b5 = Base()
        self.assertEqual(4, b5.id)

    def test_to_json_string(self):
        """Tests for to_json_string"""
        self.assertEqual('[]', Base.to_json_string(None))
        self.assertEqual('[]', Base.to_json_string({}))

    def test_from_json_string(self):
        """Tests for from_json_string"""
        self.assertEqual([], Base.from_json_string(None))
        self.assertEqual([], Base.from_json_string(''))

    def test_load_from_file(self):
        pass

    def test_save_to_file(self):
        pass

    def test_save_to_file_csv(self):
        pass

    def test_load_from_file_csv(self):
        pass
