#!/usr/bin/python3
"""City class which inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Define the class City"""
    state_id = ""
    name = ""
