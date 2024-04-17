#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

def declarative_base(*arg, **kw):
    return _declarative_base(*arg, **kw)
