#!/usr/bin/python3
"""
This module is about the base model class
"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """
    Class BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes of the class, use
        @storage variable to add a new object into @FileStorage
        private class attribute named @objects

        Attributes:
            - id (optional, str): the id of the object
            - created_at (optional, datetime): the creation date of the object
            - updated_at (optional, datetime): last modified date of the object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if not kwargs:
            models.storage.new(self)
        else:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(kwargs[key], time_format)
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """
        Update the attribute @updated_at of the base model object
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the base model object to dict

        Returns: a dictionary consisting of
        attribute names of the base model object as keys of the dictionary
        and their values as values of the dictionary
        """
        response = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                response[k] = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not v:
                    pass
                else:
                    response[k] = v
        response["__class__"] = self.__class__.__name__
        return response

    def __str__(self) -> str:
        """
        String representation of the object
        """
        return "[{0}] ({1}) {2}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
