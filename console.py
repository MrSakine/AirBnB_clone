#!/usr/bin/python3
"""
This module is the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
