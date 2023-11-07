#!/usr/bin/env python3
"""
BAse Model that contains framework for the project
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        """
        It initializes the class
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns spring rep of object"""
        return f"[{self.__class__.__name__}] ({self.id} {self.__dict__})"

    def save(self):
        """Updates when an object is changed or created"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dict rep of keys and their values"""
        dict_copy = self.__dict__
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()

        return dict_copy
