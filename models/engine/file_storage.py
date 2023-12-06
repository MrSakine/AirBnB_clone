#!/usr/bin/python3
"""
This module is about the file storage class
"""
import json
from models.base_model import BaseModel


class FileStorage():
    __file_path = "objects.json"
    __objects = {}

    def all(self):
        objects = FileStorage.__objects.items()
        return {k: str(BaseModel(**v)) for k, v in objects}

    def new(self, obj):
        key = "{0}.{1}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            print(json.dumps(FileStorage.__objects), file=file)

    def reload(self):
        try:
            FileStorage.__objects = json.load(
                open(FileStorage.__file_path, encoding="utf-8"))
        except Exception:
            pass
