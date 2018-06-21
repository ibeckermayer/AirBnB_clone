#!/usr/bin/python3
"""Defines unittests for State Model class"""
import unittest
from models.base_model import BaseModel
from models.city import City


class City_Test(unittest.TestCase):
    """Tests for City class"""

    def City_from_Base(self):
        """Tests if City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def City_attributes(self):
        """Tests for Citys attributes"""
        city = City()
        self.assertTrue("state_id" in city.__dir__())
        self.assertTrue("name" in city.__dir__())

    def city_type(self):
        """Tests for City type"""
        city = City()
        state_id = getattr(city, "state_id")
        name = getattr(city, "name")
        self.assertIsInstance(state_id, str)
        self.assertIsInstance(name, str)
