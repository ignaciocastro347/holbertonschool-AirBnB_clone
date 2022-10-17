#!/usr/bin/python3
"""files to json"""


import json
import datetime
from multiprocessing.sharedctypes import Value
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

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
        with open(self.__file_path, "w", encoding='utf-8') as file:
            save_object = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(save_object, file)

    def reload(self):
        try:
            # print("reolad1--------------")
            # print(self.__objects)
            with open(self.__file_path) as file:
                for key, value in json.load(file).items():
                    self.__objects[key] = eval(value["__class__"])(**value)
            # print("reolad2--------------")
            # print(self.__objects)
        except:
            # print("ERRORRRRRR-------------------")
            # print(err)
            pass
