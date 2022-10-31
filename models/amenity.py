#!/usr/bin/python3
"""
module amenity contains class amenity
and inherits from class BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for amenity instances
    """

    name = ""
