#!/usr/bin/python3
""" Base model """
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for id in kwargs:
                if id != "__class__":
                    if id == "created_at" or id == "updated_at":
                        i = kwargs[id]
                        datetime.strptime(m, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, id, kwargs[id])

    def to_dict(self):
        return { 
            **self.__dict__,
            "__class__": type(self).__name__,
            "created_at": str(self.created_at.isoformat()),
            "updated_at": str(self.updated_at.isoformat())
        }

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
