#!/usr/bin/python3
"""files to json"""


import json
import os.path

class FileStorage:
    """serializes to JSON and deserializes from JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.id] = obj

    def save(self):
        save_object = {}
        for key in FileStorage.__objects:
            save_object[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            file.write(json.dumps(save_object))

    def reload(self):
        FileStorage.__objects = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                json_content = file.read()
            json_content = json.loads(json_content) if json_content is not None else []
            for key, value in json_content.items():
                FileStorage.__objects[key] = value
