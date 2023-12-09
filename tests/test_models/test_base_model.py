#!/usr/bin/python3
"""
This module is all unit tests about base model class
"""
import unittest
import os
import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base Model class"""

    my_model = BaseModel()

    def test_BaseModel1(self):
        """Test attributes value of a BaseModel instance"""

        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json["name"])
        self.assertEqual(self.my_model.my_number, my_model_json["my_number"])
        self.assertEqual("BaseModel", my_model_json["__class__"])
        self.assertEqual(self.my_model.id, my_model_json["id"])

    def test_save(self):
        """Checks if save method updates the public instance instance
        attribute updated_at"""
        self.my_model.first_name = "First"
        self.my_model.save()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        first_dict = self.my_model.to_dict()

        self.my_model.first_name = "Second"
        self.my_model.save()
        sec_dict = self.my_model.to_dict()

        self.assertEqual(first_dict["created_at"], sec_dict["created_at"])
        self.assertNotEqual(first_dict["updated_at"], sec_dict["updated_at"])


class TestBaseModelSaveMethod(unittest.TestCase):
    """Unittests for testing save method of the Base Model class"""

    def test_save_object(self):
        bm = BaseModel()
        temp = bm.updated_at
        bm.save()
        self.assertTrue(bm.updated_at > temp)


class TestBaseModelToDictMethod(unittest.TestCase):
    """Unittests for testing to_dict method of the Base Model class"""

    def test_contain_known_keyword(self):
        bm = BaseModel()
        known_keys = ["id", "created_at", "updated_at", "__class__"]
        for k in known_keys:
            self.assertIsNotNone(bm.__getattribute__(k))

    def test_contain_unknown_keyword(self):
        bm = BaseModel()
        unknown_keys = ["i", "created_a", "updated_a", "__class_"]
        with self.assertRaises(AttributeError):
            for k in unknown_keys:
                bm.__getattribute__(k)

    def test_check_type_of_id_from_dict(self):
        bm = BaseModel()
        temp = bm.to_dict()
        self.assertIsInstance(temp["id"], str)

    def test_check_type_of_created_at_from_dict(self):
        bm = BaseModel()
        temp = bm.to_dict()
        self.assertIsInstance(temp["created_at"], str)

    def test_check_type_of_updated_at_from_dict(self):
        bm = BaseModel()
        temp = bm.to_dict()
        self.assertIsInstance(temp["updated_at"], str)

    def test_check_type_of_class_name_from_dict(self):
        bm = BaseModel()
        temp = bm.to_dict()
        self.assertIsInstance(temp["__class__"], str)

    def test_length_of_the_dict(self):
        self.assertEqual(len(str(BaseModel().to_dict())), 160)


class TestBaseModelStringRepresentationMethod(unittest.TestCase):
    """Unittests for testing str magic method of the Base Model class"""

    def test_str_method(self):
        bm = BaseModel()
        self.assertIn("BaseModel", str(bm))

    def test_if_empty(self):
        bm = BaseModel()
        self.assertTrue(str(bm) != "" and str(bm) is not None)

    def test_length_of_the_text(self):
        self.assertGreaterEqual(len(str(BaseModel())), 220)


class TestBaseModelStorageClass(unittest.TestCase):
    """Unittests for testing instance of FileStorage in the Base Model class"""

    def test_storage_all_method_without_instantiation(self):
        self.assertNotEqual(len(storage.all()), 0)

    def test_storage_all_method_with_instantiation(self):
        _ = BaseModel()
        self.assertGreaterEqual(len(storage.all()), 1)

    def test_storage_all_method_with_kwargs_instantiation(self):
        _ = BaseModel(**({"name": "python"}))
        self.assertGreaterEqual(len(storage.all()), 1)

    def tearDown(self) -> None:
        self.empty_file()

    def empty_file(self):
        filename = "objects.json"
        with open(filename, "w", encoding="utf-8") as file:
            print("{}", file=file, end="")


if __name__ == "__main__":
    unittest.main()
