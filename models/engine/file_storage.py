#!/usr/bin/python3
"""
This module is about the file storage class
"""
import json
from models.base_model import BaseModel


class FileStorage():
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
        objects = FileStorage.__objects.copy().items()
        return {k: BaseModel(**v) for k, v in objects}

    def new(self, obj):
        """
        Add a new object into @__objects variable

        Attributes:
        - obj (any): the object to store
        """
        key = "{0}.{1}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Save @__objects to @__file_path"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            print(json.dumps(FileStorage.__objects), file=file)

    def reload(self):
        """Get JSON contents from @__file_path"""
        try:
            FileStorage.__objects = json.load(
                open(FileStorage.__file_path, encoding="utf-8"))
        except Exception:
            pass