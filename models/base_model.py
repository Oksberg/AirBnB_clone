#!/usr/bin/python4
"""
Module for the BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """A class that all other classes inherit."""

    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    time_format = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

    def save(self):
        """
        This method saves updates to storage.
        """
        from models.engine.file_storage import storage

        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        A dict representation of the class.
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.class.name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """
        An easily human-readable representation of the class.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
