#!/usr/bin/python3
"""
    Contains amenity test cases.
"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """
    test class for amenity class
    """

    def setUP(self):
        pass

    def test_instance(self):
        """obj should be a BaseModel and amenity instance"""

        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)
        self.assertIsInstance(a1, BaseModel)

    def test_new_obj(self):
        """new diff instances should be created"""
        a1 = Amenity()
        a2 = Amenity()
        self.assertFalse(a1 is a2)

    def test_instance_dict(self):
        """intsanciate an old obj with the help of to_dict"""
        a1 = Amenity()
        my_model_dict = a1.to_dict()
        a2 = Amenity(**my_model_dict)
        self.assertEqual(a1.id, a2.id)

    def test_save(self):
        """test save method"""
        a1 = Amenity()
        old = a1.updated_at
        a1.save()
        self.assertFalse(old == a1.updated_at)

    def test_str(self):
        """test the __str__ magic method"""

        a = Amenity()
        a_str = "[Amenity] ({}) {}".format(a.id, a.__dict__)
        self.assertEqual(a_str, str(a))

    def test_attr(self):
        """test amenity attr exists"""
        a = Amenity()
        self.assertIsInstance(a.name, str)


if __name__ == "__main__":
    unittest.main(TestAmenity)
