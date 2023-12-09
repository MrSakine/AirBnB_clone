#!/usr/bin/python3
"""
This module is the entry point of the command interpreter
"""
import cmd
import sys
import re
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for the prompt that uses cmd module"""

    # INFO: task 6
    prompt = "(hbnb) "

    classes_list = ["BaseModel", "User", "Amenity", "Place", "City",
                    "State", "Review"]

    commands_list = ["create", "show", "update", "all", "destory", "count"]

    def parse_input(self, arg):
        """Parse the user input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split(".")
            cmd = cls[1].split("(")
            args = cmd[1].split(")")
            if cls[0] in self.classes_list:
                if cmd[0] in self.commands_list:
                    arg = cmd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """Help command explaination"""
        print("Usage: help <command>")

    def empty_line(self):
        """for empty line"""
        pass

     def do_quit(self, line):
        """exits the prompt: Quit command to exit the program"""
        sys.exit(1)

    def help_quit(self):
        """help for quit command"""
        print("Usage: <quit> - exits the program")

    def do_EOF(self, line):
        """Exits the program when the user uses <CTRL+D>"""
        print()
        return True

    def help_EOF(self):
        """help for EOF"""
        print("ctrl+d \texits the program")

    def do_create(self, class_name):
        """Creates an instance"""
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.classes_list:
            print("** class doesn't exist **")
        else:
            classes_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "City": City,
                "Place": Place,
                "Amenity": Amenity,
                "State": State,
                "Review": Review
            }
            model = classes_dict[class_name]()
            print(model.id)
            model.save()

    def do_show(self, arg):
        """SHow instance that been passed"""



if __name__ == "__main__":
    HBNBCommand().cmdloop()
