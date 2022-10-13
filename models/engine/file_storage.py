#!/usr/bin/python3
"""files to json"""


from models.base_model import BaseModel
import json

class FileStorage:
    """serializes to JSON and deserializes from JSON"""

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open("self.__file_path" , "w") as write:
            return write.write(json.dumps(self.__objects, write))

    def reload(self):
        if self.__file_path is None:
            return