#!/usr/bin/python3
"""
This module is about the file storage class
"""
import json


class FileStorage:
    """
    File storage class definition
    """

    """Class attribute to store the file name"""
    __file_path = "objects.json"

    """
    Class attribute to store the JSON representation in
    Python from @__file_path
    """
    __objects = {}

    def all(self):
        """Load JSON as objects in Python"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object into @__objects variable

        Attributes:
        - obj (any): the object to store
        """
        key = "{0}.{1}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Save @__objects to @__file_path"""
        objects = FileStorage.__objects
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump({k: objects[k].to_dict() for k in objects.keys()}, file)

    def reload(self):
        """Get JSON contents from @__file_path"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                objs = json.load(file)
                temp = {}
                for k, v in objs.items():
                    class_name = v.get("__class__")
                    if class_name:
                        cls = globals().get(class_name)
                        if cls:
                            temp[k] = cls(
                                **{
                                    k1: v1
                                    for k1, v1 in v.items()
                                    if k1 != "__class__"
                                }
                            )
                FileStorage.__objects = temp
        except FileNotFoundError:
            pass