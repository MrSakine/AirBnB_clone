#!/usr/bin/python3
"""
This module is about the state model class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherit from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """init"""
        BaseModel.__init__(self, *args, **kwargs)
