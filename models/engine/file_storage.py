#!/usr/bin/python3
"""files to json"""


from models.base_model import BaseModel
import json
import os.path

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
        with open(self.__file_path, "w", encoding='utf-8') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        if os.path.exists(self.__file_path):

            with open(file.json, "r", encoding="utf-8") as read:
                self.__objects = json.load(read)
