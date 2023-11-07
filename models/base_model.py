#!/usr/bin/python3
"""Defines the BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel of the airBnB project"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel
        Args:
            *args (any): Unused
            **kwargs (dict): Key/value pairs of attributes
        """
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        mydict = self.__dict__.copy()
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["__class__"] = self.__class__.__name__
        return mydict

    def __str__(self):
        """Return the str representation of the BaseModel instance"""
        cname = elf.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)
