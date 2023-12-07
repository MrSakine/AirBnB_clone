#!/usr/bin/python3
""" Defines tests for the Place class, defined in <place module> """
from models.place import Place
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """ Define Place attributes and methods tests """
    def setUp(self):
        """ Instantiate User test objects """
        self.place = Place()

    # test that the class correctly instantiates
    def test_place_instantiation(self):
        """ test that Place class correctly instantiates """
        self.assertTrue(isinstance(self.place, Place))

    # test that all public class attributes are included & in correct types
    def test_place_isAttribute_city_id(self):
        """ test that Place class contains city_id public attribute """
        self.assertTrue(getattr(self.place, 'city_id', None) is not None)

    def test_place_isStr_city_id(self):
        """ test that city_id public attribute is str """
        self.assertTrue(isinstance(getattr(self.place, 'city_id', None), str))

    def test_place_isAttribute_user_id(self):
        """ test that Place class contains user_id public attribute """
        self.assertTrue(getattr(self.place, 'user_id', None) is not None)

    def test_place_isStr_user_id(self):
        """ test that user_id public attribute is str """
        self.assertTrue(isinstance(getattr(self.place, 'user_id', None), str))

    def test_place_isAttribute_name(self):
        """ test that Place class contains name public attribute """
        self.assertTrue(getattr(self.place, 'name', None) is not None)

    def test_place_isStr_name(self):
        """ test that name public attribute is str """
        self.assertTrue(isinstance(getattr(self.place, 'name', None), str))

    def test_place_isAttribute_description(self):
        """ test that Place class contains description public attribute """
        self.assertTrue(getattr(self.place, 'description', None) is not None)

    def test_place_isStr_description(self):
        """ test that description public attribute is str """
        self.assertTrue(isinstance(getattr(self.place, 'description', None),
                        str))

    def test_place_isAttribute_number_rooms(self):
        """ test that Place class contains number_rooms public attribute """
        self.assertTrue(getattr(self.place, 'number_rooms', None) is not None)

    def test_place_isInt_number_rooms(self):
        """ test that number_rooms public attribute is an integer """
        self.assertTrue(isinstance(getattr(self.place, 'number_rooms', None),
                        int))

    def test_place_isAttribute_number_bathrooms(self):
        """ test that Place class has number_bathrooms public attribute """
        self.assertTrue(getattr(self.place, 'number_bathrooms', None)
                        is not None)

    def test_place_isInt_number_bathrooms(self):
        """ test that number_bathrooms public attribute is an integer """
        self.assertTrue(isinstance(getattr(self.place, 'number_bathrooms',
                        None), int))

    def test_place_isAttribute_max_guest(self):
        """ test that Place class contains max_guest public attribute """
        self.assertTrue(getattr(self.place, 'max_guest', None) is not None)

    def test_place_isInt_max_guest(self):
        """ test that max_guest public attribute is an integer """
        self.assertTrue(isinstance(getattr(self.place, 'max_guest', None),
                        int))

    def test_place_isAttribute_price_by_night(self):
        """ test that Place class contains price_by_night public attribute """
        self.assertTrue(getattr(self.place, 'price_by_night', None)
                        is not None)

    def test_place_isInt_price_by_night(self):
        """ test that price_by_night public attribute is an integer """
        self.assertTrue(isinstance(getattr(self.place, 'price_by_night', None),
                        int))

    def test_place_isAttribute_latitude(self):
        """ test that Place class contains latitude public attribute """
        self.assertTrue(getattr(self.place, 'latitude', None) is not None)

    def test_place_isFloat_latitude(self):
        """ test that latitude public attribute is a float """
        self.assertTrue(isinstance(getattr(self.place, 'latitude', None),
                        float))

    def test_place_isAttribute_longitude(self):
        """ test that Place class contains longitude public attribute """
        self.assertTrue(getattr(self.place, 'longitude', None) is not None)

    def test_place_isFloat_longitude(self):
        """ test that longitude public attribute is a float """
        self.assertTrue(isinstance(getattr(self.place, 'longitude', None),
                        float))

    def test_place_isAttribute_amenity_ids(self):
        """ test that Place class contains amenity_ids public attribute """
        self.assertTrue(getattr(self.place, 'amenity_ids', None) is not None)

    def test_place_islist_amenity_ids(self):
        """ test that amenity_ids public attribute is a list (of strs) """
        self.assertTrue(isinstance(getattr(self.place, 'amenity_ids', None),
                        list))

    # test that the class inherits from BaseModel
    def test_place_isinstance_of_BaseModel(self):
        """ test that Place class inherits from BaseModel """
        self.assertTrue(isinstance(self.place, BaseModel))
