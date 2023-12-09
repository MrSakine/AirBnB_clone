#!/usr/bin/python3
"""Defines tests for the State class, defined in <models>"""
from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    """ Define State attributes and methods tests """

    def setUp(self):
        """ Instantiate State test objects """
        self.state = State()

    # test that the class correctly instantiates
    def test_state_instantiation(self):
        """ test that State class correctly instantiates """
        self.assertTrue(isinstance(self.state, State))

    # test that all public class attributes are included
    def test_state_is_attribute_name(self):
        """ test that State class contains name public attribute """
        self.assertTrue(getattr(self.state, 'name', None) is not None)

    def test_state_is_str_name(self):
        """ test that name public attribute is a string """
        self.assertTrue(isinstance(getattr(self.state, 'name', None),
                        str))

    def test_state_is_not_attribute_nonExistent(self):
        """ test that State class does Not contain public attribute,
        nonExistent """
        self.assertTrue(getattr(self.state, 'nonExistent', None) is None)

    # test that the class inherits from BaseModel
    def test_state_is_instance_of_base_model(self):
        """ test that State class inherits from BaseModel """
        self.assertTrue(isinstance(self.state, BaseModel))
