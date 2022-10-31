#!/usr/bin/python3
"""
module city contains class City
and inherits from class BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for city instances
    """

    state_id = ""
    name = ""
