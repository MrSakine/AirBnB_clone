#!/usr/bin/python3
"""amenity.py"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherit from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """init"""
        BaseModel.__init__(self, *args, **kwargs)
