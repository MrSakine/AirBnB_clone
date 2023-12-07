#!/usr/bin/python3
""" Defines tests for the User class, defined in <user module> """
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """ Define User attributes and methods tests """
    def setUp(self):
        """ Instantiate User test objects """
        self.user = User()

    # test that the class correctly instantiates
    def test_user_instantiation(self):
        """ test that User class correctly instantiates """
        self.assertTrue(isinstance(self.user, User))

    # test that all public class attributes are included
    def test_user_isAttribute_email(self):
        """ test that User class contains email public attribute """
        self.assertTrue(getattr(self.user, 'email', None) is not None)

    def test_user_isAttribute_first_name(self):
        """ test that User class contains first_name public attribute """
        self.assertTrue(getattr(self.user, 'first_name', None) is not None)

    def test_user_isAttribute_password(self):
        """ test that User class contains password public attribute """
        self.assertTrue(getattr(self.user, 'password', None) is not None)

    def test_user_isAttribute_last_name(self):
        """ test that User class contains last_name public attribute """
        self.assertTrue(getattr(self.user, 'last_name', None) is not None)

    # test that the class inherits from BaseModel
    def test_user_isinstance_of_BaseModel(self):
        """ test that User class correctly instantiates """
        self.assertTrue(isinstance(self.user, BaseModel))
