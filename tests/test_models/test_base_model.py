#!/usr/bin/python3
"""
Contains basemodel test cases.
"""

from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    test class for basemodel class
    """

    def test_instance(self):
        """obj should be a BaseModel instance"""

        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_new_obj(self):
        """new diff instances should be created"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertFalse(b1 is b2)

    def test_instance_dict(self):
        """intsanciate an old obj with the help of to_dict"""
        b1 = BaseModel()
        my_model_dict = b1.to_dict()
        b2 = BaseModel(**my_model_dict)
        self.assertEqual(b1.id, b2.id)

    def test_save(self):
        """test save method"""
        b1 = BaseModel()
        old = b1.updated_at
        b1.save()
        self.assertNotEqual(old, b1.updated_at)

    def test_str(self):
        """test the __str__ majic method"""

        b = BaseModel()
        b_str = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(b_str, str(b))

    def test_id(self):
        """It should have a string id"""
        b1 = BaseModel()

        self.assertIsNotNone(b1.id)
        self.assertIsInstance(b1.id, str)

    def test_created_at(self):
        """It should have a datetime created_at attribute"""
        b1 = BaseModel()

        self.assertIsNotNone(b1.created_at)
        self.assertIsInstance(b1.created_at, datetime)

    def test_updated_at(self):
        """It should have a datetime updated_at attribute"""
        b1 = BaseModel()

        self.assertIsNotNone(b1.updated_at)
        self.assertIsInstance(b1.updated_at, datetime)

    def test_to_dict(self):
        """It should have a datetime updated_at attribute"""
        b1 = BaseModel()

        self.assertIsInstance(b1.to_dict(), dict)


if __name__ == "__main__":
    unittest.main(TestBaseModel)
