#!/usr/bin/python3
"""Defines unittests for Place Model class"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class Place_Test(unittest.TestCase):
    """Tests for Place class"""

    def Place_from_Base(self):
        """Tests if Place inherits from BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def Place_attributes(self):
        """Tests for Place attributes"""
        place = Place()
        self.assertTrue("city_id" in place.__dir__())
        self.assertTrue("user_id" in place.__dir__())
        self.assertTrue("name" in place.__dir__())
        self.assertTrue("description" in place.__dir__())
        self.assertTrue("number_rooms" in place.__dir__())
        self.assertTrue("number_bathrooms" in place.__dir__())
        self.assertTrue("max_guest" in place.__dir__())
        self.assertTrue("price_by_night" in place.__dir__())
        self.assertTrue("latitude" in place.__dir__())
        self.assertTrue("longitude" in place.__dir__())
        self.assertTrue("amenity_ids" in place.__dir__())

    def place_type(self):
        """Tests for Place type"""
        place = Place()
        city_id = getattr(place, "city_id")
        self.assertIsInstance(city_id, str)
        user_id = getattr(place, "user_id")
        self.assertIsInstance(user_id, str)
        name = getattr(place, "name")
        self.assertIsInstance(name, str)
        description = getattr(place, "description")
        self.assertIsInstance(description, str)
        number_rooms = getattr(place, "number_rooms")
        self.assertIsInstance(number_rooms, int)
        number_bathrooms = getattr(place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)
        max_guest = getattr(place, "max_guest")
        self.assertIsInstance(max_guest, int)
        price_by_night = getattr(place, "price_by_night")
        self.assertIsInstance(price_by_night, int)
        latitude = getattr(place, "latitude")
        self.assertIsInstance(latitude, float)
        longitude = getattr(place, "longitude")
        self.assertIsInstance(longitude, float)
        amenity_ids = getattr(place, "amenity_ids")
        self.assertIsInstance(amenity_ids, list)
