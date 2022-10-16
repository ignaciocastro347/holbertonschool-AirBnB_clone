#!/usr/bin/python3
"""files to json"""


import json
import os.path

class FileStorage:
    """serializes to JSON and deserializes from JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        save_object = {}
        # print(self.__objects)
        for key in self.__objects:
            save_object[key] = self.__objects[key].to_dict()
            if type(save_object[key]) == "datetime":
                save_object[key] = save_object[key].isoformat()
        with open(self.__file_path, "w", encoding='utf-8') as file:
            file.write(json.dumps(save_object))

    def reload(self):
        try:
            with open(self.__file_path) as file:
                for key, value in json.load(file).items():
                    self.__objects[key] = value
        except:
            pass
        # self.__objects = {}
        # if os.path.exists(self.__file_path):
        #     with open(self.__file_path, "r", encoding="utf-8") as file:
        #         json_content = file.read()
        #     json_content = json.loads(json_content) if json_content is not None else []
        #     for key, value in json_content.items():
        #         self.__objects[key] = value
