#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from os import getenv
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

# Define a base class for declarative class definitions
if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # create instance attributes from kwargs
        for key, value in kwargs.items():
            if key == "created_at" or key == "updated_at":
                # convert to datatime type
                self.__dict__[key] = datetime.strptime(
                    value, "%Y-%m-%dT%H:%M:%S.%f"
                )
            elif key != "__class__":  # other attributes except __class__
                self.__dict__[key] = kwargs[key]

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update(
            {"__class__": (str(type(self)).split(".")[-1]).split("'")[0]}
        )
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        # remove _sa_instance_state key from dict
        dictionary.pop("_sa_instance_state", None)

        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        from models import storage

        storage.delete(self)
