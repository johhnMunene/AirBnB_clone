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
        if kwargs:
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
