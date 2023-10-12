#!/usr/bin/python3

"""
Filestorage class
"""
import json
from model.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary"""
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

