#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel"""
        Dform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs :
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, Dform))
                else:
                    setattr(self, key, value)

    def save(self):
        # Implement the save method logic here

        def to_dict(self):
            obj_dict = {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
            # Add other attributes you want to include in the dictionary
        }
        return obj_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return str(self.to_dict())

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a new BaseModel instance from a dictionary representation"""
        if "__class__" in obj_dict:
            if obj_dict["__class__"] == cls.__name__:
                obj_dict.pop("__class__")
                if "created_at" in obj_dict:
                    obj_dict["created_at"] = datetime.strptime(obj_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if "updated_at" in obj_dict:
                    obj_dict["updated_at"] = datetime.strptime(obj_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                return cls(**obj_dict)
        return None
