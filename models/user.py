#!/usr/bin/python3
"""module that defines user class"""


from models.base_model import BaseModel


class User(BaseModel):
    """user definition by various attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
