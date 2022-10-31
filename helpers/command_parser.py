#!/usr/bin/python3
"""Parses an arg into a format that can be processed by
cmd.
"""
import re


class CommandParser:
    """This will parse any command args and reformat it
    if needed.
    """

    @staticmethod
    def isparsable(arg=""):
        """Checks if an `arg` can be parsed

        Args:
            arg(str): The command argument
        """

        if type(arg) is not str:
            return False
        pattern = r"^\w+?\.\w+?\(.*\)$"
        return re.search(pattern, arg) is not None

    @staticmethod
    def parse(arg=""):
        """Parses and `arg` into compatible cmd format

        Args:
            arg(str): The command argument
        """

        if not CommandParser.isparsable(arg):
            return arg

        model = re.findall(r"^(\w+)", arg)[0]
        cmd = re.findall(r"\.(\w+)", arg)[0]
        raw_arg = re.findall(r"""(\(["\',0-9A-Za-z\-_{}: ]+\))""", arg)
        parsed = ""

        if len(raw_arg) > 0:
            temp = raw_arg[0].replace("(", "").replace(")", "")
            raw_arg = temp.split(",")
            o_id = raw_arg[0]
            raw_arg = temp[len(o_id):]
            o_id = o_id.replace('"', "")

            if raw_arg.startswith(","):
                raw_arg = (raw_arg[1:]).strip()
            if not raw_arg.startswith("{"):
                raw_arg = raw_arg.split(",")
                arg_len = len(raw_arg)
                for i in range(0, arg_len):
                    data = raw_arg[i].strip()
                    if i != arg_len - 1:
                        data = data.replace('"', "")
                    raw_arg[i] = data
                raw_arg = ' '.join(raw_arg)
            parsed = "{} {}".format(o_id, raw_arg)

        return "{} {} {}".format(cmd, model, parsed).strip()
