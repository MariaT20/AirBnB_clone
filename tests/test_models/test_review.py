#!/usr/bin/python3
"""
Contains Review test cases.
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    test cases for Review class
    """

    def setUp(self):
        """sets up test data"""

        self.obj = Review()

    def test_obj(self):
        """It should be an instance of Review"""

        self.assertIsInstance(self.obj, Review)
        self.assertTrue(self.obj, issubclass(Review, BaseModel))

    def test_attr(self):
        """It should have a text attr"""

        self.assertIsInstance(self.obj.text, str)
        self.assertEqual(self.obj.text, "")


if __name__ == "__main__":
    unittest.main(TestReview)
