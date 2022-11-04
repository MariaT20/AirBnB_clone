#!/usr/bin/python3
"""
Contains place test cases.
"""

import unittest
import os
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """
    test class for basemodel class
    """

    def test_instance(self):
        """obj should be a BaseModel and user instance"""

        p1 = Place()
        self.assertIsInstance(p1, Place)
        self.assertIsInstance(p1, BaseModel)

    def test_new_obj(self):
        """new diff instances should be created"""
        p1 = Place()
        p2 = Place()
        self.assertFalse(p1 is p2)

    def test_instance_dict(self):
        """intsanciate an old obj with the help of to_dict"""
        p1 = Place()
        my_model_dict = p1.to_dict()
        p2 = Place(**my_model_dict)
        self.assertEqual(p1.id, p2.id)

    def test_save(self):
        """test save method"""
        p1 = Place()
        old = p1.updated_at
        p1.save()
        self.assertFalse(old == p1.updated_at)

    def test_str(self):
        """test the __str__ magic method"""

        p = Place()
        p_str = "[Place] ({}) {}".format(p.id, p.__dict__)
        self.assertEqual(p_str, str(p))

    def test_attr(self):
        """test Place attr exists"""
        p = Place()
        self.assertIsInstance(p.city_id, str)
        self.assertIsInstance(p.user_id, str)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.description, str)
        self.assertIsInstance(p.number_rooms, int)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.max_guest, int)
        self.assertIsInstance(p.price_by_night, int)
        self.assertIsInstance(p.latitude, float)
        self.assertIsInstance(p.longitude, float)
        self.assertIsInstance(p.amenity_ids, list)


if __name__ == "__main__":
    unittest.main(TestPlace)
