#!/usr/bin/python3
"""
This module is about the initialization of models package
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
