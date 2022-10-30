#!/usr/bin/python3
"""
Contains user test cases.
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    test class for basemodel class
    """

    def test_instance(self):
        """obj should be a BaseModel and user instance"""

        u1 = User()
        self.assertIsInstance(u1, User)
        self.assertIsInstance(u1, BaseModel)

    def test_new_obj(self):
        """new diff instances should be created"""
        u1 = User()
        u2 = User()
        self.assertFalse(u1 is u2)

    def test_instance_dict(self):
        """intsanciate an old obj with the help of to_dict"""
        u1 = User()
        my_model_dict = u1.to_dict()
        u2 = User(**my_model_dict)
        self.assertEqual(u1.id, u2.id)

    def test_save(self):
        """test save method"""
        u1 = User()
        old = u1.updated_at
        u1.save()
        self.assertFalse(old == u1.updated_at)

    def test_str(self):
        """test the __str__ magic method"""

        u = User()
        u_str = "[User] ({}) {}".format(u.id, u.__dict__)
        self.assertEqual(u_str, str(u))

    def test_attr(self):
        """test user attr exists"""
        u = User()
        self.assertIsInstance(u.email, str)
        self.assertIsInstance(u.password, str)
        self.assertIsInstance(u.first_name, str)
        self.assertIsInstance(u.last_name, str)


if __name__ == "__main__":
    unittest.main(TestUser)
