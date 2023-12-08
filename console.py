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

    def __init__(self):
        """init"""
        cmd.Cmd.__init__(self)
        self.classes = {
            "BaseModel": self.create_base_model,
            "User": self.create_user,
            "State": self.create_state,
            "City": self.create_city,
            "Place": self.create_place,
            "Amenity": self.create_amenity,
            "Review": self.create_review,
        }
        self.all_instance_regex = r"^[a-zA-Z]+\.all\(\)$"
        self.count_instance_regex = r"^[a-zA-Z]+\.count\(\)$"
        self.show_instance_regex = r"^[a-zA-Z]+\.show\("
        self.destroy_instance_regex = r"^[a-zA-Z]+\.destroy\("
        self.update_instance_regex = r"^[a-zA-Z]+\.update\("

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

    def create_base_model(self, **kwargs):
        """Create a new instance of base model"""
        if kwargs:
            return BaseModel(**kwargs)
        else:
            return BaseModel()

    def create_user(self, **kwargs):
        """create a new istance of user"""
        if kwargs:
            return User(**kwargs)
        else:
            return User()

    def create_state(self, **kwargs):
        """create a new instance of state"""
        if kwargs:
            return State(**kwargs)
        else:
            return State()

    def create_city(self, **kwargs):
        """create a new instance of city"""
        if kwargs:
            return City(**kwargs)
        else:
            return City()

    def create_place(self, **kwargs):
        """create a new instance of place"""
        if kwargs:
            return Place(**kwargs)
        else:
            return Place()

    def create_amenity(self, **kwargs):
        """create a new instance of amenity"""
        if kwargs:
            return Amenity(**kwargs)
        else:
            return Amenity()

    def create_review(self, **kwargs):
        """create a new instance of review"""
        if kwargs:
            return Review(**kwargs)
        else:
            return Review()

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
                    for obj, _ in objs.items():
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

    def convert_value(self, value):
        value = value.strip('"')
        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            pass
        return value

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
                                for k, _ in (string.to_dict()).items():
                                    if k == args[2]:
                                        if len(args) > 3:
                                            attr_val = self.convert_value(
                                                args[3]
                                            )
                                            setattr(string, args[2], attr_val)
                                            string.save()
                                        else:
                                            print("** value missing **")
                                        break
                            else:
                                print("** attribute name missing **")
                            break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def default(self, line):
        """Handle unnamed commands"""
        is_count = re.match(self.count_instance_regex, line)
        if is_count:
            self.count_instance(line)
        elif re.match(self.all_instance_regex, line):
            self.all_instances(line)
        elif re.match(self.show_instance_regex, line):
            pass
        elif re.match(self.destroy_instance_regex, line):
            self.destroy_instance(line)
        elif re.match(self.update_instance_regex, line) and ", {" in line:
            self.update_instance_from_dictionary(line)
        elif re.match(self.update_instance_regex, line) and ', "' in line:
            # update instance through attributes
            # <class name>.update(<id>, <attribute name>, <attribute value>)
            pass
        else:
            print("Unknown syntax: {}".format(self.parseline(line)[2]))

    def count_instance(self, line):
        """Count the instance of a class name from file objects"""
        parsed_lines = line.split(".")
        class_name = parsed_lines[0]
        if class_name not in (self.classes).keys():
            print("** class doesn't exist **")
            return
        print(
            sum(
                [
                    1
                    for _, v in storage.all().items()
                    for k1, v1 in v.to_dict().items()
                    if k1 == "__class__" and v1 == class_name
                ]
            )
        )

    def all_instances(self, line):
        """
        Retrieve all instances of a class by using: <class name>.all()
        """
        parse_line = line.split(".")
        class_name = parse_line[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        instances = []
        for _, v in storage.all().items():
            for k, v1 in v.to_dict().items():
                if k == "__class__" and v1 == class_name:
                    instances.append(str(v))
        print(instances)

    def destroy_instance(self, line: str):
        """
        Destroy an instance based on his ID: <class name>.destroy(<id>)
        """
        class_name = line.split(".")[0]
        if class_name not in (self.classes).keys():
            print("** class doesn't exist **")
            return
        start_occurence = line.find('"')
        end_occurence = line.find('"', start_occurence + 1)
        object_id = line[start_occurence + 1:end_occurence]
        if start_occurence == -1 or end_occurence == -1:
            print("** invalid argument **")
            return
        objects = storage.all()
        for obj, _ in objects.items():
            if obj.split(".")[1] == object_id:
                del objects[obj]
                storage.save()
                break
        else:
            print("** no instance found **")

    def update_instance_from_dictionary(self, line: str):
        """
        Update an instance based on his ID with a dictionary:
        <class name>.update(<id>, <dictionary representation>)
        """
        class_name = line.split(".")[0]
        if class_name not in (self.classes).keys():
            print("** class doesn't exist **")
            return
        start_occurence = line.find('"', 0, line.find(","))
        end_occurence = line.find('"', start_occurence + 1, line.find(","))
        if start_occurence == -1 or end_occurence == -1:
            print("** invalid format for the id **")
            return
        object_id = line[start_occurence + 1:end_occurence]
        start_occurence = line.find("{")
        end_occurence = line.find("}", start_occurence + 1)
        if start_occurence == -1 or end_occurence == -1:
            print("** invalid format for the dictionary **")
            return
        dictionary = line[start_occurence:end_occurence + 1]
        objects = storage.all()
        for obj, value in objects.items():
            if obj.split(".")[1] == object_id:
                for k, v in eval(dictionary).items():
                    setattr(value, k, v)
                storage.save()
                break
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
