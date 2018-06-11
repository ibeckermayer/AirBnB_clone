#!/usr/bin/python3
"""Review class which inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Define the Review class"""
    place_id = ""
    user_id = ""
    text = ""
