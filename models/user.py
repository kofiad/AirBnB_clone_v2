#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String


class User(BaseModel, Base):
    if models.is_type == "db":
        __tablename__ = "users"

        email = Column(String(128), nullable=False),
        password = Column(String(128), nullable=False),
        first_name = Column(String(128), nullable=False),
        last_name = Column(String(128), nullable=False),
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''