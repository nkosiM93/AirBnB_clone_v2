#!usr/bin/python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place, place_amenity
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """The engine for storing data in a database"""

    __engine = None
    __session = None


    def __init__(self):
        
        """Initializes the SQL database storage"""
        self.__engine = create_engine('mysql+mysqldb://'
                                      f"{os.get_env('BNB_MYSQL_USER')}:"
                                      f"{os.get_env('HBNB_MYSQL_PWD')}"
                                      f"@{'os.get_env(HBNB_MYSQL_HOST)'}:3306/"
                                      f"{os.get_env(HBNB_MYSQL_DB)}, "
                                      "pool_pre_ping=True")
        if os.get_env('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """dictionary of models present in storage"""
        objects = dict()
        all_classes = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for class_type in all_classes:
                query = self.__session.query(class_type)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj

        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj
        return objects

    def new(self, obj):
        """Adding New objects to DB"""

        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh()
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        self.__session.commit()

    def delete(self):
        """Removes an object from the storage database"""
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete(
                synchronize_session='fetch')
            self.__session.commit()

    def reload(self):
        """Load all info from the specific table in database"""

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self._session = scoped_session(Session)()































