#!/usr/bin/python3
"""state.py"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherit from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """init"""
        BaseModel.__init__(self, *args, **kwargs)
