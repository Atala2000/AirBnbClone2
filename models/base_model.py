#!/usr/bin/env python3
"""
BAse Model that contains framework for the project
"""
from uuid import uuid4
from datetime import datetime

date_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        It initializes the class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key in ["created_at", "updated_at"] and isinstance(value, str):
                    setattr(self, key, datetime.strptime(value, date_format))
        else:
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
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        for key in ["created_at", "updated_at"]:
            if key in dict_copy and isinstance(dict_copy[key], datetime):
                dict_copy[key] = dict_copy[key].isoformat()
        return dict_copy
