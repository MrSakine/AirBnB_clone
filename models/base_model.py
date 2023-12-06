#!/usr/bin/python3
"""
This module is the base model class
"""
import uuid
import models
import time
from datetime import datetime


class BaseModel():
    """
    Class BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs) -> None:
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
        self.updated_at = datetime.now()

        if len(kwargs) == 0:
            models.storage.new(self)
        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(
                            self, k, datetime.strptime(
                                v, "%Y-%m-%dT%H:%M:%S.%f")
                        )
                    else:
                        setattr(self, k, v)
        else:
            pass

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
        for k, v in vars(self).items():
            if k == "created_at" or k == "updated_at":
                response[k] = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                response[k] = v
        response["__class__"] = self.__class__.__name__
        return (response)

    def __str__(self) -> str:
        """
        String representation of the object
        """
        return (
            "[{0}] ({1}) {2}".format(
                self.__class__.__name__, self.id, self.__dict__
            )
        )

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        models.storage.new(self)