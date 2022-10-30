#!/usr/bin/python3
"""Contains test cases for CommandParser"""

import unittest
from helpers.command_parser import CommandParser


class TestCommandParser(unittest.TestCase):
    """Defines test cases for CommandParser"""

    def test_isparsable(self):
        """It should return True for `User.show("test-id-1234")`
        """

        result = CommandParser.isparsable('User.show("test-id-1234")')
        self.assertTrue(result)

    def test_isparsable_wrong_format(self):
        """It should return False for `show User "test-id-1234"`
        """

        result = CommandParser.isparsable('show User "test-id-1234"')
        self.assertFalse(result)

    def test_isparsable_None(self):
        """It should return false for None
        """

        result = CommandParser.isparsable(None)
        self.assertFalse(result)

    def test_isparsable_None(self):
        """It should return false for int
        """

        result = CommandParser.isparsable(101)
        self.assertFalse(result)

    def test_isparsable_float(self):
        """It should return false for float
        """

        result = CommandParser.isparsable(10.1)
        self.assertFalse(result)

    def test_isparsable_empty_str(self):
        """It should return false for empty str
        """

        result = CommandParser.isparsable("")
        self.assertFalse(result)

    def test_parse_show(self):
        """It should parse `User.show("test-id-1234")`
        """

        result = CommandParser.parse('User.show("test-id-1234")')
        self.assertEqual(result, 'show User test-id-1234')

    def test_parse_destroy(self):
        """It should parse `User.destroy("test-id-1234")`
        """

        result = CommandParser.parse('User.destroy("test-id-1234")')
        self.assertEqual(result, 'destroy User test-id-1234')

    def test_parse_all(self):
        """It should parse `User.all()`
        """

        result = CommandParser.parse('User.all()')
        self.assertEqual(result, 'all User')

    def test_parse_count(self):
        """It should parse `User.count()`
        """

        result = CommandParser.parse('User.count()')
        self.assertEqual(result, 'count User')

    def test_parse_update(self):
        """It should parse `User.update("test-id-1234", "first_name", "john")`
        """
        text = 'User.update("test-id-1234", "first_name", "john")'
        expected = 'update User test-id-1234 first_name "john"'
        result = CommandParser.parse(text)
        self.assertEqual(expected, result)

    def test_parse_update_dict(self):
        """It should parse
        `User.update("test-id-1234", {"first_name": "john"})`
        """
        text = 'User.update("test-id-1234", {"first_name": "john"})'
        expected = 'update User test-id-1234 {"first_name": "john"}'
        result = CommandParser.parse(text)
        self.assertEqual(expected, result)

    def test_parse_None(self):
        """It should return None
        """

        self.assertEqual(CommandParser.parse(None), None)

    def test_parse_empty_str(self):
        """It should return empty str
        """

        self.assertEqual(CommandParser.parse(""), "")

    def test_parse_int(self):
        """It should return 101
        """

        self.assertEqual(CommandParser.parse(101), 101)

    def test_parse_float(self):
        """It should return 10.1
        """

        self.assertEqual(CommandParser.parse(10.1), 10.1)


if __name__ == "__main__":
    unittest.main(TestCommandParser)
