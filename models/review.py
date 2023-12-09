#!/usr/bin/python3
"""
This module is about the review model class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that inherit from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize attributes of the class"""
        BaseModel.__init__(self, *args, **kwargs)
