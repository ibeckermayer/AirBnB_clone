#!/usr/bin/python3
"""Defines unittests for Amenity Model class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class Amenity_Test(unittest.TestCase):
    """Tests for Amenity class"""

    def Amenity_from_Base(self):
        """Tests if Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def Amenity_attributes(self):
        """Tests for Amenity Attributes"""
        amenity = Amenity()
        self.assertTrue("name" in amenity.__dir__())

    def Amentiy_type(self):
        """Tests for Amenity type"""
        amenity = Amenity()
        amenity_name = getattr(amenity, "name")
        self.assertIsInstance(amenity_name, str)
