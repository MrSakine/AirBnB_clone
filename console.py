#!/usr/bin/python3
"""
This module is the entry point of the command interpreter
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for the prompt that uses cmd module"""

    # INFO: task 6
    prompt = "(hbnb) "

    def __init__(self) -> None:
        """init"""
        cmd.Cmd.__init__(self)
        self.classes = {
            "BaseModel": self.create_BaseModel,
        }

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

    # INFO: Task 7 Starts Here.

    def create_BaseModel(self, **kwargs):
        """Create a new instance from BaseModel"""
        if kwargs:
            return BaseModel(**kwargs)
        else:
            return BaseModel()

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if line:
            for c, m in (self.classes).items():
                if c in line:
                    new_m = m()
                    new_m.save()
                    print(new_m.id)
                    break
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation
        of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        if line:
            args = line.split()
            if args[0] and args[0] not in (self.classes).keys():
                print("** class doesn't exist **")
            else:
                if len(args) > 1:
                    objects = storage.all()
                    key = "{}.{}".format(args[0], args[1])
                    for obj, string in objects.items():
                        if obj == key:
                            print(string)
                            break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if line:
            args = line.split()
            if args[0] and args[0] not in (self.classes).keys():
                print("** class doesn't exist **")
            else:
                if len(args) > 1:
                    objs = storage.all()
                    key = "{}.{}".format(args[0], args[1])
                    for obj, string in objs.items():
                        if obj == key:
                            del objs[obj]
                            storage.save()
                            break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        objs = storage.all()
        obj_list = []
        if line:
            for cls in (self.classes).keys():
                if line == cls:
                    for obj, value in objs.items():
                        name = (obj.split("."))[0]
                        if name == line:
                            obj_list.append(str(value))
                    print(obj_list)
                    break
            else:
                print("** class doesn't exist **")
        else:
            for obj, value in objs.items():
                obj_list.append(str(value))
            print(obj_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        if line:
            args = line.split()
            if args[0] and args[0] not in (self.classes).keys():
                print("** class doesn't exist **")
            else:
                if len(args) > 1:
                    objects = storage.all()
                    key = "{}.{}".format(args[0], args[1])
                    for obj, string in objects.items():
                        if obj == key:
                            if len(args) > 2:
                                for k, val in (string.to_dict()).items():
                                    if k == args[2]:
                                        if len(args) > 3:
                                            attr_val = type(val)(args[3])
                                            setattr(string, args[2], attr_val)
                                            string.save()
                                        else:
                                            print("** value missing **")
                                        break
                                else:
                                    if len(args) > 3:
                                        setattr(srting, args[2], args[3])
                                        string.save()
                                    else:
                                        print("** value missing **")
                            else:
                                print("** attribute name missing **")
                            break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
