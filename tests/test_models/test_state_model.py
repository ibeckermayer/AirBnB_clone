#!/usr/bin/python3
"""Defines unittests for State Model class"""
import unittest
from models.base_model import BaseModel
from models.state import State


class State_Test(unittest.TestCase):
    """Tests for State class"""

    def State_from_Base(self):
        """Tests if State inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def State_attributes(self):
        """Tests for States attributes"""
        state = State()
        self.assertTrue("name" in state.__dir__())

    def state_type(self):
        """Tests for state type"""
        state = State()
        state_name = getattr(state, "name")
        self.assertIsInstance(state_name, str)
