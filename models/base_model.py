#!/usr/bin/python3
"""Base Model"""

import uuid
from datetime import datetime


class BaseModel:
    """Base Model Class"""

    def __init__(self, *args, **kwargs):
        """Arguments"""
        if len(kwargs) != 0:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for key in kwargs:
                if key != "__class__":
                    if key == "created_at" or id == "updated_at":
                        i = kwargs[key]
                        datetime.strptime(i, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, kwargs[key])

    def to_dict(self):
        """Return a Dictionary"""
        return { 
            **self.__dict__,
            "__class__": type(self).__name__,
            "created_at": str(self.created_at.isoformat()),
            "updated_at": str(self.updated_at.isoformat())
        }

    def __str__(self):
        """Prints string representation of class"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """update instance of class"""
        self.updated_at = datetime.now()
