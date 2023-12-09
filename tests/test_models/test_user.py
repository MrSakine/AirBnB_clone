#!/usr/bin/python3
"""
This module is all unit tests about user class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for testing instantiation of the Base Model class"""

    def setUp(self) -> None:
        self.user = User()

    def test_user_exist(self):
        """Test if class user exist"""
        self.assertTrue(isinstance(self.user, User))

    def test_user_email_attribute(self):
        """Tests user email attribute"""
        self.assertTrue(getattr(self.user, "email", None) is not None)

    def test_user_firstname_attribute(self):
        """Tests user firstname attribute"""
        self.assertTrue(getattr(self.user, "first_name", None) is not None)

    def test_user_lastname_attribute(self):
        """Tests user lastname attribute"""
        self.assertTrue(getattr(self.user, "last_name", None) is not None)

    def test_user_password_attribute(self):
        """Tests user password attribute"""
        self.assertTrue(getattr(self.user, "password", None) is not None)

    def test_user_email_attribute_instance(self):
        """Tests user email attribute instance"""
        self.assertTrue(isinstance(getattr(self.user, "email", None), str))

    def test_user_firstname_attribute_instance(self):
        """Tests user firstname attribute instance"""
        self.assertTrue(
            isinstance(
                getattr(
                    self.user,
                    "first_name",
                    None
                ),
                str
            )
        )

    def test_user_lastname_attribute_instance(self):
        """Tests user lastname attribute instance"""
        self.assertTrue(isinstance(getattr(self.user, "last_name", None), str))

    def test_user_password_attribute_instance(self):
        """Tests user password attribute instance"""
        self.assertTrue(isinstance(getattr(self.user, "password", None), str))


if __name__ == "__main__":
    unittest.main()
