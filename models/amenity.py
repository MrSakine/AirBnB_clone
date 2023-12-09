#!/usr/bin/python3
"""
This module is about the amenity model class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherit from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize attributes of the class"""
        BaseModel.__init__(self, *args, **kwargs)
