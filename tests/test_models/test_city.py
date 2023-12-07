#!/usr/bin/python3
""" Defines tests for the City class, defined in <city module> """
from models.city import City
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """ Define City attributes and methods tests """
    def setUp(self):
        """ Instantiate City test objects """
        self.city = City()

    # test that the class correctly instantiates
    def test_user_instantiation(self):
        """ test that City class correctly instantiates """
        self.assertTrue(isinstance(self.city, City))

    # test that all public class attributes are included
    def test_city_isAttribute_name(self):
        """ test that City class contains name public attribute """
        self.assertTrue(getattr(self.city, 'name', None) is not None)

    def test_city_isAttribute_state_id(self):
        """ test that City class contains state_id public attribute """
        self.assertTrue(getattr(self.city, 'state_id', None) is not None)

    def test_city_isNotAttribute_password(self):
        """ test that City class does NOT contain a random public attribute,
        password """
        self.assertTrue(getattr(self.city, 'password', None) is None)

    # test that the class inherits from BaseModel
    def test_city_isinstance_of_BaseModel(self):
        """ test that City class inherits from BaseModel """
        self.assertTrue(isinstance(self.city, BaseModel))
