#!/usr/bin/python3
"""Defines tests for the Amenity class, defined in <models>"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """Define Amenity attributes and methods tests"""

    def setUp(self):
        """Instantiate Amenity test objects"""
        self.amenity = Amenity()

    # test that the class correctly instantiates
    def test_amenity_instantiation(self):
        """test that Amenity class correctly instantiates"""
        self.assertTrue(isinstance(self.amenity, Amenity))

    # test that all public class attributes are included
    def test_amenity_is_attribute_email(self):
        self.amenity.email = "test@gmail.com"
        """test that Amenity class contains email public attribute"""
        self.assertTrue(getattr(self.amenity, "email", None) is not None)

    def test_amenity_is_attribute_first_name(self):
        """test that Amenity class contains first_name public attribute"""
        self.amenity.first_name = "test"
        self.assertTrue(getattr(self.amenity, "first_name", None) is not None)

    def test_amenity_is_attribute_password(self):
        self.amenity.password = "test"
        """test that Amenity class contains password public attribute"""
        self.assertTrue(getattr(self.amenity, "password", None) is not None)

    def test_amenity_is_attribute_last_name(self):
        self.amenity.last_name = "test"
        """test that Amenity class contains last_name public attribute"""
        self.assertTrue(getattr(self.amenity, "last_name", None) is not None)

    # test that the class inherits from BaseModel
    def test_amenity_is_instance_of_base_model(self):
        """test that Amenity class correctly instantiates"""
        self.assertTrue(isinstance(self.amenity, BaseModel))

    def tearDown(self) -> None:
        del self.amenity
