#!/usr/bin/python3
"""This module defines validation Rules."""


from models import storage
from helpers.class_loader import ClassLoader


class CommandValidator:
    """Provides validation Rules."""

    @staticmethod
    def canUseModel(arg):
        """Returns True if the command can be processed,
        Otherwise, returns False

        Args:
            arg(str): The argument to be validated
        """

        if type(arg) is not str:
            return False

        if arg == "":
            print("** class name missing **")
            return False

        model = ClassLoader.load(arg)
        if model is None:
            print("** class doesn't exist **")
            return False

        return True

    @staticmethod
    def canDoCommand(arg):
        """Returns True if the command can be processed,
        Otherwise, returns False

        Args:
            arg(str): The argument to be validated
        """

        if type(arg) is not str:
            return False

        if arg == "":
            print("** class name missing **")
            return False

        args = arg.strip().split(" ")
        model = ClassLoader.load(args[0])
        if model is None:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key, None)

        if obj is None:
            print("** no instance found **")
            return False

        return True

    @staticmethod
    def canDoUpdate(arg):
        """Returns True if an update can be done, False
        Otherwise.

        Args:
            arg(str): The argument to be validated

        Update Format:
        <class name> <id> <attribute name> "<attribute value>"
        """

        if not CommandValidator.canDoCommand(arg):
            return False

        args = arg.strip().split(" ")

        if len(args) < 3:
            print("** attribute name missing **")
            return False

        if len(args) < 4:
            print("** value missing **")
            return False

        return True
