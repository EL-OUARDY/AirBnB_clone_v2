#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """city class representation"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship(
            "Place", backref="cities", cascade="all, delete-orphan"
        )

    else:  # file storage case
        name = ""
        state_id = ""
