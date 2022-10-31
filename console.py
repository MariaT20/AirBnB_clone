#!/usr/bin/python3
"""This module contains the console interface for interacting
with the Application.
"""

import cmd
import re
import json
from helpers.command_parser import CommandParser
from models import storage
from helpers.command_validator import CommandValidator
from helpers.class_loader import ClassLoader


class HBNBCommand(cmd.Cmd):
    """The Application console class. Contains all the
    commands that this application can execute
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Ensures that an empty line + ENTER shouldn’t
        execute anything"""

        return False

    def do_quit(self, arg):
        """Quit command to exit the program
        """

        return True

    def do_EOF(self, arg):
        """End of File command to exit the program
        """

        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of given class, saves it to json
        file and print the id
        """

        if not CommandValidator.canUseModel(arg):
            return False
        model = ClassLoader.load(arg)
        obj = model()
        obj.save()
        print("{}".format(obj.id))

    def do_show(self, arg):
        """ Prints the string representation of an instance based
        on the class name and id
        """

        if not CommandValidator.canDoCommand(arg):
            return False

        args = arg.strip().split(" ")
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key, None)
        print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """

        if not CommandValidator.canDoCommand(arg):
            return False

        args = arg.strip().split(" ")
        key = "{}.{}".format(args[0], args[1])
        del storage.all()[key]
        storage.save()

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute
        """

        if not CommandValidator.canDoUpdate(arg):
            return False

        args = arg.strip().split(" ")
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key, None)
        raw_dict_list = re.findall(r"\{.+?\}", arg)
        to_update = {}
        if len(raw_dict_list) > 0:
            try:
                raw_dict_list[0] = raw_dict_list[0].replace("'", '"')
                to_update = json.loads(raw_dict_list[0])
            except Exception:
                print("failed")
                pass
        else:
            key = args[2].replace('"', '')
            value = ' '.join(args[3:])
            quoted_value = value.split('"')
            if len(quoted_value) > 1:
                value = quoted_value[1].strip()
            to_update[key] = int(value) if value.isnumeric() else value

        for key in to_update:
            value = to_update[key]
            try:
                attribute_type = type(getattr(obj, key))
                setattr(obj, key, attribute_type(value))
            except AttributeError:
                setattr(obj, key, value)
            except ValueError:
                pass
        obj.save()

    def do_all(self, arg=""):
        """Prints all string representation of all
        instances based or not on the class name
        """

        list_o = []
        if arg == "":
            objs = storage.all()
            for key in objs:
                list_o.append(str(objs[key]))
        else:
            if not CommandValidator.canUseModel(arg):
                return False
            objs = storage.all()
            for key in objs:
                if arg in key:
                    list_o.append(str(objs[key]))
        print(list_o)

    def do_count(self, arg=""):
        """retrieve the number of instances of a class: <class name>.count()"""

        if not CommandValidator.canUseModel(arg):
            return False
        count = 0
        for key in storage.all():
            if key.startswith(arg):
                count += 1
        print(count)

    def precmd(self, line=""):
        """Hook to process command before is executed"""

        return CommandParser.parse(line)

    def onecmd(self, line=""):
        """Overrides CMD onecmd"""

        return cmd.Cmd.onecmd(self, CommandParser.parse(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
