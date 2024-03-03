#!/usr/bin/python3
"""
This class manages storage using SQLAlchemy
with a mysql+mysqldb database connection
"""


from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages storage in a MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """class constructor"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@{host}/{database}",
            pool_pre_ping=True,
        )

        # drop all tables if the environment is set to test
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary of all the objects of a class"""
        if not self.__session:
            self.reload()
        objects_dict = {}
        if type(cls) is str:  # target class passed as string
            cls = self.get_app_classes().get(cls, None)
        if cls:
            for obj in self.__session.query(cls):
                objects_dict[obj.__class__.__name__ + "." + obj.id] = obj
        else:
            # query all types of objects
            for c in self.get_app_classes().values():
                for obj in self.__session.query(c):
                    objects_dict[obj.__class__.__name__ + "." + obj.id] = obj
        return objects_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads objects from the database"""
        # create all tables in the database
        Base.metadata.create_all(self.__engine)
        # create the current database session
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        self.__session = scoped_session(session_factory)

    def get_app_classes(self):
        """get a dictionary that holds all app classes | name: reference"""

        return {
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
