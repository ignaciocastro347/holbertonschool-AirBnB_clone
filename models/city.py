#!/usr/bin/python3
"""City class that inherits from BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """City public class Attributes"""
    state_id = ""
    name = ""
