#!/usr/bin/python3
"""
This module is all unit tests about file storage class
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json
from datetime import datetime


class TestFileStorageInstantiation(unittest.TestCase):
    """Unittests for testing Storage"""

    my_model = BaseModel()

    def test_object_initialization(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_class_instance(self):
        """Check instance"""
        self.assertIsInstance(storage, FileStorage)

    def test_store_BaseModel(self):
        """Test save and reload functions"""
        self.my_model.full_name = "BaseModel Instance"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict["__class__"] + "." + bm_dict["id"]
        self.assertEqual(key in all_objs, True)

    def test_store_BaseModel2(self):
        """Test save, reload and update functions"""
        self.my_model.my_name = "First name"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict["__class__"] + "." + bm_dict["id"]

        self.assertEqual(key in all_objs, True)
        self.assertEqual(bm_dict["my_name"], "First name")

        create1 = bm_dict["created_at"]
        update1 = bm_dict["updated_at"]

        self.my_model.my_name = "Second name"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create2 = bm_dict["created_at"]
        update2 = bm_dict["updated_at"]

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(bm_dict["my_name"], "Second name")

    def test_has_attributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(FileStorage, "_FileStorage__file_path"), True)
        self.assertEqual(hasattr(FileStorage, "_FileStorage__objects"), True)

    def test_save(self):
        """verify if JSON exists"""
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """test if reload"""
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())

    def test_save_FileStorage(self):
        """Test if 'new' method is working good"""
        var1 = self.my_model.to_dict()
        new_key = var1["__class__"] + "." + var1["id"]
        storage.save()
        with open("objects.json", "r") as fd:
            var2 = json.load(fd)
        new = var2[new_key]

        # Round datetime values to the same precision (e.g., seconds)
        for key in new:
            if isinstance(var1[key], str) and "T" in var1[key]:
                var1[key] = str(
                    datetime.fromisoformat(var1[key]).replace(microsecond=0)
                )
            if isinstance(new[key], str) and "T" in new[key]:
                new[key] = str(
                    datetime.fromisoformat(new[key]).replace(microsecond=0)
                )

        for key in new:
            self.assertEqual(var1[key], new[key])


if __name__ == "__main__":
    unittest.main()
