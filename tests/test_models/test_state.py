#!/usr/bin/python3
"""
Contains State test cases.
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    test cases for State class
    """

    def setUp(self):
        """sets up test data"""

        self.obj = State()

    def test_obj(self):
        """It should be an instance of State"""

        self.assertIsInstance(self.obj, State)
        self.assertTrue(self.obj, issubclass(State, BaseModel))

    def test_attr(self):
        """It should have a name attr"""

        self.assertIsInstance(self.obj.name, str)
        self.assertEqual(self.obj.name, "")


if __name__ == "__main__":
    unittest.main(TestState)
