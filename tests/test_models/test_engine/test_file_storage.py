#!/usr/bin/python3
"""
This module is all unit tests about file storage class
"""
import unittest
import models
from models.engine.file_storage import FileStorage


class TestFileStorageInstantiation(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def test_object_initialization(self):
        self.assertEqual(type(FileStorage()), FileStorage)


if __name__ == "__main__":
    unittest.main()
