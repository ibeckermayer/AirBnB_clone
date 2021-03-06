#!/usr/bin/python3
"""Module for file storage
"""
import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage(object):
    """serializes instances to a JSON file and deserializes JSON
       file to instances

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): empty but will store all objects by <class name>.id
                          (ex: to store a BaseModel object with id=12121212,
                           the key will be BaseModel.12121212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects

        Returns:
            dict: the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Attributes:
            obj (object): the object to be set
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        ser_dict = {}
        if self.__objects:
            for key, obj in self.__objects.items():
                ser_dict[key] = obj.to_dict()
            with open(self.__file_path, 'w') as f:
                json.dump(ser_dict, f)
        else:
            try:
                os.remove(self.__file_path)
            except FileNotFoundError:
                pass

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
           exists ; otherwise, do nothing)
        """
        try:
            with open(self.__file_path, 'r') as f:
                deser_dict = {}
                deser_dict = json.load(f)
                for key, val in deser_dict.items():
                    self.__objects[key] = eval(val["__class__"])(**val)
        except FileNotFoundError:
            pass
