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
        save_object = {}
        for key in self.__objects:
            save_object[key] = self.__objects[key].to_dict()
        with open("self.__file_path", "w", encoding='utf-8') as write:
            json.dumps(save_object, write)

    def reload(self):
        if self.__file_path is None:
            return
