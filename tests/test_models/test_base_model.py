#!/usr/bin/python3
"""
This module is all unit tests about base model class
"""
import unittest
import subprocess
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base Model class"""

    def setUp(self) -> None:
        pass

    def test_id_initialization(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_created_at_initialization(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_updated_at_initialization(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_two_objects(self):
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(bm.id != bm2.id)

    def test_initialization_without_kwargs(self):
        bm = BaseModel()
        self.assertTrue(len(bm.__dict__) == 3)

    def test_initialization_with_one_kwarg(self):
        bm = BaseModel(**({"name": "python"}))
        self.assertEqual(bm.__dict__.__len__(), 4)

    def test_initialization_with_multiple_kwargs(self):
        bm = BaseModel(**(
            {
                "name": "python",
                "surname": "3.8",
                "father": "C",
                "students": "alx"
            }
        ))
        self.assertGreater(bm.__dict__.__len__(), 3)


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

    def test_storage_save_and_reload_method_without_instance(self):
        self.empty_file()
        storage.reload()
        _all = storage.all()
        self.assertEqual(len(_all), 0)

    def tearDown(self) -> None:
        self.empty_file()

    def empty_file(self):
        filename = "objects.json"
        with open(filename, "w", encoding="utf-8") as file:
            print("{}", file=file, end="")


if __name__ == "__main__":
    unittest.main()