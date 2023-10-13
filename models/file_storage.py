#!/usr/bin/python3

"""
Filestorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json

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
    def save(self):
                """
        Serializes __objects to the JSON file (__file_path).
        """
    serialized_data = {}
    for key ,obj in FileStorage .__objects.items():
                serialized_data[key] = obj.to_dict()
                with open(FileStorage.__file_path,'w') as file:
                    json.dump(serialized_data, file)
    def reload(self):
        """
        Deserializes the JSON file (__file_path) to __objects if it exists.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    
                    obj = o (**obj_data)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass