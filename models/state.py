#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="states")
    else:  # file storage case
        name = ""

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """fs getter attribute that returns City instances"""
            from models import storage

            cities = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
