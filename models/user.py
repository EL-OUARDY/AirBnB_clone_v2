#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """user class representation"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            "Place", backref="user", cascade="all, delete-orphan"
        )
        reviews = relationship(
            "Review", backref="user", cascade="all, delete-orphan"
        )

    else:  # file storage case
        email = ""
        password = ""
        first_name = ""
        last_name = ""
