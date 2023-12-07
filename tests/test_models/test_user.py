#!/usr/bin/python3
"""
This module is all unit tests about user class
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unittests for testing instantiation of the Base Model class"""

    def setUp(self) -> None:
        self.user = User()

    def test_user_exist(self):
        """Test if class user exist"""
        self.assertTrue(isinstance(self.user, User))

    def test_user_attributes(self):
        """Tests user attributes"""
        # EMAIL
        self.assertTrue(getattr(self.user, "email", None) is not None)
        self.assertTrue(isinstance(getattr(self.user, "email", None), str))
        # FIRST_NAME
        self.assertTrue(getattr(self.user, "first_name", None) is not None)
        self.assertTrue(isinstance(getattr(self.user, "first_name", None), str))
        # LAST_NAME
        self.assertTrue(getattr(self.user, "last_name", None) is not None)
        self.assertTrue(isinstance(getattr(self.user, "last_name", None), str))
        # PASSWORD
        self.assertTrue(getattr(self.user, "password", None) is not None)
        self.assertTrue(isinstance(getattr(self.user, "password", None), str))


if __name__ == "__main__":
    unittest.main()
