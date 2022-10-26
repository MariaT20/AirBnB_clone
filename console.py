#!/usr/bin/python3

"""
The console of the AirBnB 
"""

import cmd

class HbnbConsole(cmd.Cmd):
    """
    Custom CLI prompt for the console
    """
    prompt = '(hbnb) '

    def do_EOF(self, args):
        """ END OF FILE """
        return True

    def do_quit(self, args):
        """ Quits the console

        Args:
            args - inputs an argument for quitting the console
        """
        return True

if __name__ == '__main__':
        HbnbConsole().cmdloop()
