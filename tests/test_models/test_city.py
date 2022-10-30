#!/usr/bin/python3
"""
Contains user test cases.
"""

import unittest
import os
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """
    test class for city class
    """

    def test_instance(self):
        """obj should be a BaseModel and city instance"""

        c1 = City()
        self.assertIsInstance(c1, City)
        self.assertIsInstance(c1, BaseModel)

    def test_new_obj(self):
        """new diff instances should be created"""
        c1 = City()
        c2 = City()
        self.assertFalse(c1 is c2)

    def test_instance_dict(self):
        """intsanciate an old obj with the help of to_dict"""
        c1 = City()
        my_model_dict = c1.to_dict()
        c2 = City(**my_model_dict)
        self.assertEqual(c1.id, c2.id)

    def test_save(self):
        """test save method"""
        c1 = City()
        old = c1.updated_at
        c1.save()
        self.assertFalse(old == c1.updated_at)

    def test_str(self):
        """test the __str__ magic method"""

        c = City()
        c_str = "[City] ({}) {}".format(c.id, c.__dict__)
        self.assertEqual(c_str, str(c))

    def test_attr(self):
        """test city attr exists"""
        c = City()
        self.assertIsInstance(c.state_id, str)
        self.assertIsInstance(c.name, str)


if __name__ == "__main__":
    unittest.main(TestCity)
