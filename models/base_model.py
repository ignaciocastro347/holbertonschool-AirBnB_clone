#!/usr/bin/python3
""" Base model """
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def to_dict(self):
        return { **self.__dict__, "__class__": type(self).__name__ }

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
