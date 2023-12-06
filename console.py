#!/usr/bin/python3
"""
This module is the entry point of the command interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Class for the prompt that uses cmd module"""

    prompt = "(hbnb) "

    def __init__(self) -> None:
        """init"""
        cmd.Cmd.__init__(self)

    def do_quit(self, line):
        """exits the prompt: Quit command to exit the program"""
        sys.exit(1)

    def help_quit(self):
        """help for quit command"""
        print("quit \texits the program")

    def do_EOF(self, line):
        """Exits the program when the user uses <CTRL+D>"""
        print()
        return True

    def help_EOF(self):
        """help for EOF"""
        print("ctrl+d \texits the program")

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
