#!/usr/bin/python3
"""user.py"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs) -> None:
        """init"""
        BaseModel.__init__(self, *args, **kwargs)
