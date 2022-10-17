#!/usr/bin/python3
"""Base Model"""

from  uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Base Model Class"""

    def __init__(self, *args, **kwargs):
        """Arguments"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value

    def to_dict(self):
        """Return a Dictionary"""
        new_dict = dict(self.__dict__)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = type(self).__name__
        return new_dict

    def __str__(self):
        """Prints string representation of class"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """update instance of class"""
        self.updated_at = datetime.now()
        models.storage.save()
