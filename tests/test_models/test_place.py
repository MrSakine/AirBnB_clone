#!/usr/bin/python3
""" Defines tests for the Place class, defined in <place module> """
from models.place import Place
from models.base_model import BaseModel
import unittest
import datetime


class TestPlace(unittest.TestCase):
    """Define Place attributes and methods tests"""

    p = Place()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.p)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.p, Place)

    def test_has_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.p, "city_id"))
        self.assertTrue(hasattr(self.p, "user_id"))
        self.assertTrue(hasattr(self.p, "name"))
        self.assertTrue(hasattr(self.p, "description"))
        self.assertTrue(hasattr(self.p, "number_rooms"))
        self.assertTrue(hasattr(self.p, "number_bathrooms"))
        self.assertTrue(hasattr(self.p, "max_guest"))
        self.assertTrue(hasattr(self.p, "price_by_night"))
        self.assertTrue(hasattr(self.p, "latitude"))
        self.assertTrue(hasattr(self.p, "longitude"))
        self.assertTrue(hasattr(self.p, "amenity_ids"))
        self.assertTrue(hasattr(self.p, "id"))
        self.assertTrue(hasattr(self.p, "created_at"))
        self.assertTrue(hasattr(self.p, "updated_at"))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.p.city_id, str)
        self.assertIsInstance(self.p.user_id, str)
        self.assertIsInstance(self.p.name, str)
        self.assertIsInstance(self.p.description, str)
        self.assertIsInstance(self.p.number_rooms, int)
        self.assertIsInstance(self.p.number_bathrooms, int)
        self.assertIsInstance(self.p.max_guest, int)
        self.assertIsInstance(self.p.price_by_night, int)
        self.assertIsInstance(self.p.latitude, float)
        self.assertIsInstance(self.p.longitude, float)
        self.assertIsInstance(self.p.amenity_ids, list)
        self.assertIsInstance(self.p.id, str)
        self.assertIsInstance(self.p.created_at, datetime.datetime)
        self.assertIsInstance(self.p.updated_at, datetime.datetime)

    def setUp(self):
        """Instantiate Place test objects"""
        self.place = Place()

    # test that the class correctly instantiates
    def test_place_instantiation(self):
        """test that Place class correctly instantiates"""
        self.assertTrue(isinstance(self.place, Place))

    # test that all public class attributes are included & in correct types
    def test_place_is_attribute_city_id(self):
        """test that Place class contains city_id public attribute"""
        self.assertTrue(getattr(self.place, "city_id", None) is not None)

    def test_place_is_str_city_id(self):
        """test that city_id public attribute is str"""
        self.assertTrue(isinstance(getattr(self.place, "city_id", None), str))

    def test_place_is_attribute_user_id(self):
        """test that Place class contains user_id public attribute"""
        self.assertTrue(getattr(self.place, "user_id", None) is not None)

    def test_place_is_str_user_id(self):
        """test that user_id public attribute is str"""
        self.assertTrue(isinstance(getattr(self.place, "user_id", None), str))

    def test_place_is_attribute_name(self):
        """test that Place class contains name public attribute"""
        self.assertTrue(getattr(self.place, "name", None) is not None)

    def test_place_is_str_name(self):
        """test that name public attribute is str"""
        self.assertTrue(isinstance(getattr(self.place, "name", None), str))

    def test_place_is_attribute_description(self):
        """test that Place class contains description public attribute"""
        self.assertTrue(getattr(self.place, "description", None) is not None)

    def test_place_is_str_description(self):
        """test that description public attribute is str"""
        self.assertTrue(
            isinstance(getattr(self.place, "description", None), str)
        )

    def test_place_is_attribute_number_rooms(self):
        """test that Place class contains number_rooms public attribute"""
        self.assertTrue(getattr(self.place, "number_rooms", None) is not None)

    def test_place_is_int_number_rooms(self):
        """test that number_rooms public attribute is an integer"""
        self.assertTrue(
            isinstance(getattr(self.place, "number_rooms", None), int)
        )

    def test_place_is_attribute_number_bathrooms(self):
        """test that Place class has number_bathrooms public attribute"""
        self.assertTrue(
            getattr(self.place, "number_bathrooms", None) is not None
        )

    def test_place_is_int_number_bathrooms(self):
        """test that number_bathrooms public attribute is an integer"""
        self.assertTrue(
            isinstance(getattr(self.place, "number_bathrooms", None), int)
        )

    def test_place_is_attribute_max_guest(self):
        """test that Place class contains max_guest public attribute"""
        self.assertTrue(getattr(self.place, "max_guest", None) is not None)

    def test_place_is_int_max_guest(self):
        """test that max_guest public attribute is an integer"""
        self.assertTrue(isinstance(getattr(self.place, "max_guest", None), int))

    def test_place_is_attribute_price_by_night(self):
        """test that Place class contains price_by_night public attribute"""
        self.assertTrue(getattr(self.place, "price_by_night", None) is not None)

    def test_place_is_int_price_by_night(self):
        """test that price_by_night public attribute is an integer"""
        self.assertTrue(
            isinstance(getattr(self.place, "price_by_night", None), int)
        )

    def test_place_is_attribute_latitude(self):
        """test that Place class contains latitude public attribute"""
        self.assertTrue(getattr(self.place, "latitude", None) is not None)

    def test_place_is_float_latitude(self):
        """test that latitude public attribute is a float"""
        self.assertTrue(
            isinstance(getattr(self.place, "latitude", None), float)
        )

    def test_place_is_attribute_longitude(self):
        """test that Place class contains longitude public attribute"""
        self.assertTrue(getattr(self.place, "longitude", None) is not None)

    def test_place_is_float_longitude(self):
        """test that longitude public attribute is a float"""
        self.assertTrue(
            isinstance(getattr(self.place, "longitude", None), float)
        )

    def test_place_is_attribute_amenity_ids(self):
        """test that Place class contains amenity_ids public attribute"""
        self.assertTrue(getattr(self.place, "amenity_ids", None) is not None)

    def test_place_is_list_amenity_ids(self):
        """test that amenity_ids public attribute is a list (of strs)"""
        self.assertTrue(
            isinstance(getattr(self.place, "amenity_ids", None), list)
        )

    # test that the class inherits from BaseModel
    def test_place_is_instance_of_base_model(self):
        """test that Place class inherits from BaseModel"""
        self.assertTrue(isinstance(self.place, BaseModel))


if __name__ == "__main__":
    unittest.main()
