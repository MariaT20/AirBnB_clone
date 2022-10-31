#!/usr/bin/python3
"""
module user contains class user
and inherits from class BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class for user instances
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
