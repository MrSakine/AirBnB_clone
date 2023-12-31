#!/usr/bin/python3
"""
This module is about the file storage class
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """File storage class definition"""

    __file_path = "objects.json"
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
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Save @__objects to @__file_path"""
        dicts = {}
        for key, value in FileStorage.__objects.items():
            dicts[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(dicts, file)

    def reload(self):
        """Get JSON contents from @__file_path"""
        models_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "State": State,
            "Review": Review,
        }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                try:
                    for _, value in json.load(file).items():
                        self.new(models_dict[value["__class__"]](**value))
                except Exception:
                    pass
