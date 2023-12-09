#!/usr/bin/python3
"""
This module is the entry point of the command interpreter
"""
import cmd
import sys
import re
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """Class for the prompt that uses cmd module"""

    # INFO: task 6
    prompt = "(hbnb) "

    classes_list = [
        "BaseModel",
        "User",
        "Amenity",
        "Place",
        "City",
        "State",
        "Review",
    ]

    commands_list = ["create", "show", "update", "all", "destroy", "count"]

    def precmd(self, arg):
        """Parse the user input"""
        if "." in arg and "(" in arg and ")" in arg:
            cls = arg.split(".")
            comand = cls[1].split("(")
            args = comand[1].split(")")
            if cls[0] in self.classes_list and comand[0] in self.commands_list:
                arg = comand[0] + " " + cls[0] + " " + args[0]
        return arg

    def help_help(self):
        """Help command explaination"""
        print("Usage: help <command>")

    def empty_line(self):
        """for empty line"""
        pass

    def do_quit(self, line):
        """exits the prompt: Quit command to exit the program"""
        return True

    def help_quit(self):
        """help for quit command"""
        print("Usage: <quit> - exits the program")

    def do_EOF(self, line):
        """Exits the program when the user uses <CTRL+D>"""
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
                "Review": Review,
            }
            model = classes_dict[class_name]()
            print(model.id)
            model.save()

    def do_show(self, arg):
        """Show instance that been passed"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(" ")

        if args[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for _, value in objs.items():
                object_name = value.__class__.__name__
                object_id = value.id
                if object_name == args[0] and object_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destorys an instance that been passed"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(" ")

        if args[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for key, value in objs.items():
                object_name = value.__class__.__name__
                object_id = value.id
                if object_name == args[0] and object_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return

            print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances of the given class or all instances"""
        objs = storage.all()
        instances = []

        if not arg:
            # If no argument is provided, print all instances
            for _, value in objs.items():
                instances.append(value.__str__())
        else:
            # If argument is provided, print instances of the specified class
            args = arg.split(" ")
            if args[0] not in self.classes_list:
                print("** class doesn't exist **")
                return

            for _, value in objs.items():
                object_name = value.__class__.__name__
                if object_name == args[0]:
                    instances.append(value.__str__())

        print(instances)

    def do_update(self, arg):
        """Updates instances based on the class name and id"""

        if not arg:
            print("** class name missing **")
            return

        argument = ""
        for a in arg.split(","):
            argument = argument + a

        args = shlex.split(argument)

        if args[0] not in self.classes_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for _, o in objs.items():
                object_name = o.__class__.__name__
                object_id = o.id
                if object_name == args[0] and object_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(o, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_count(self, class_name):
        """Count the instance of a class name from file objects"""
        count = 0
        objs = storage.all()
        for key, _ in objs.items():
            class_ = key.split(".")
            if class_[0] == class_name:
                count = count + 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
