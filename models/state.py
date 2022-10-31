#!/usr/bin/python3
"""
module state contains class state
and inherits from class BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for state instances
    """

    name = ""
