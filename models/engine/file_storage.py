#!/usr/bin/python3
"""files to json"""
import json


class FileStorage:
    """serializes to JSON and deserializes from JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        save_object = {}

        for key in self.__objects:
            save_object[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(save_object, file)

    def reload(self):
        try:
            with open(self.__file_path) as file:
                for key, value in json.load(file).items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except:
            pass
