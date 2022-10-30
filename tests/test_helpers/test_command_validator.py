#!/usr/bin/python3
"""Contains test cases for CommandValidator"""

import unittest
from helpers.command_validator import CommandValidator
from models.user import User


class TestCommandValidator(unittest.TestCase):
    """Defines test cases for CommandValidator"""

    def test_canUseModel(self):
        """It should return true for `BaseModel`
        """

        self.assertTrue(CommandValidator.canUseModel("BaseModel"))

    def test_canUseModel_invalid(self):
        """It should return false for `MyModel`
        """

        self.assertFalse(CommandValidator.canUseModel("MyModel"))

    def test_canUseModel_empty(self):
        """It should return false for empty str
        """

        self.assertFalse(CommandValidator.canUseModel(""))

    def test_canUseModel_numbers(self):
        """It should return false for numbers
        """

        self.assertFalse(CommandValidator.canUseModel(101))
        self.assertFalse(CommandValidator.canUseModel(10.1))

    def test_canDoCommand(self):
        """It should return true for `User id`
        """

        user = User()
        cmd = "User {}".format(user.id)
        self.assertTrue(CommandValidator.canDoCommand(cmd))

    def test_canDoCommand_empty(self):
        """It should return false for empty str
        """

        self.assertFalse(CommandValidator.canDoCommand(""))

    def test_canDoCommand_None(self):
        """It should return false for None
        """

        self.assertFalse(CommandValidator.canDoCommand(None))

    def test_canDoCommand_number(self):
        """It should return false for numbers
        """

        self.assertFalse(CommandValidator.canDoCommand(101))
        self.assertFalse(CommandValidator.canDoCommand(10.1))

    def test_canDoUpdate(self):
        """It should return true for `User id "attribute" "value"`
        """

        user = User()
        cmd = 'User {} "age" 89'.format(user.id)
        self.assertTrue(CommandValidator.canDoCommand(cmd))

    def test_canDoUpdate_None(self):
        """It should return false for None
        """

        self.assertFalse(CommandValidator.canDoCommand(None))

    def test_canDoUpdate_empty(self):
        """It should return false for empty str
        """

        self.assertFalse(CommandValidator.canDoCommand(""))

    def test_canDoUpdate_number(self):
        """It should return false for number
        """

        self.assertFalse(CommandValidator.canDoCommand(101))
        self.assertFalse(CommandValidator.canDoCommand(10.1))


if __name__ == "__main__":
    unittest.main(TestCommandValidator)
