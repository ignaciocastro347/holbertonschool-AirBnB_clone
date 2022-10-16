#!/usr/bin/python3
"""Base Model"""

import uuid
from datetime import datetime


class BaseModel:
    """Base Model Class"""

    def __init__(self, *args, **kwargs):
        """Arguments"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        self[key] = datetime.fromisoformat(value)
                    self[key] = kwargs[key]

    def to_dict(self):
        """Return a Dictionary"""
        instance_dict = dict(self.__dict__)
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['__class__'] = type(self).__name__
        return instance_dict

    def __str__(self):
        """Prints string representation of class"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """update instance of class"""
        self.updated_at = datetime.now()
