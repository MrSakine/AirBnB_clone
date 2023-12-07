#!/usr/bin/python3
"""
This module is about the city model class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherit from BaseModel"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """init"""
        BaseModel.__init__(self, *args, **kwargs)