#!/usr/bin/python3
"""Defines tests for the Review class, defined in <models>"""
from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReview(unittest.TestCase):
    """ Define Review attributes and methods tests """

    def setUp(self):
        """ Instantiate Review test objects """
        self.review = Review()

    # test that the class correctly instantiates
    def test_review_instantiation(self):
        """ test that Review class correctly instantiates """
        self.assertTrue(isinstance(self.review, Review))

    # test that all public class attributes are included
    def test_review_is_attribute_email(self):
        """ test that Review class contains email public attribute """
        self.assertTrue(getattr(self.review, 'place_id', None) is not None)

    def test_review_is_attribute_first_name(self):
        """ test that Review class contains first_name public attribute """
        self.assertTrue(getattr(self.review, 'user_id', None) is not None)

    def test_review_is_attribute_password(self):
        """ test that Review class contains password public attribute """
        self.assertTrue(getattr(self.review, 'text', None) is not None)

    def test_review_is_attribute_last_name(self):
        """ test that Review class contains last_name public attribute """
        self.assertTrue(getattr(self.review, 'last_name', None) is None)

    # test that the class inherits from BaseModel
    def test_review_is_instance_of_base_model(self):
        """ test that Review class correctly instantiates """
        self.assertTrue(isinstance(self.review, BaseModel))
