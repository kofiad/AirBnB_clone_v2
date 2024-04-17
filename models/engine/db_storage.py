#!/usr/bin/python3
"""
This module, defines a class, to manage storage
database, for hbnb clone..
"""
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import models


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Creating an instance. of the storage
        database, to create the engine.
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB"),
                                             pool_pre_ping=True))

        if getenv("HBNB_ENV ") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        A query on the current database session
        """
        if not cls:
            data_list = self.__session.query(Amenity)
            data_list.extend(self.__session.query(City))
            data_list.extend(self.__session.query(Place))
            data_list.extend(self.__session.query(Review))
            data_list.extend(self.__session.query(State))
            data_list.extend(self.__session.query(User))
        else:
            data_list = self.__session.query(cls)
        return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                for obj in data_list}

    def new(self, obj):
        """
        Method,: to add the object, to the
        current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Method,: to commit all changes, to the
        current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete method;
        current database session obj, if not None.
        """
        # obj = cls.id, dentro de una clase, sería una fila de esa clase
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        call remove() method on private session attribute
        """
        self.__session.close()
