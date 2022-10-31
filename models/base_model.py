#!/usr/bin/python3

import uuid
from datetime import datetime

"""The BaseModel"""


class BaseModel:
    """Defining the BaseModel"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """should print:[<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the attr updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict.update({"__class__": self.__class__.__name__})
#       OR new_dict["__class__"] = self.__class__.__name__}
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict


# def save_to_JSON(self, filename =""):
#   """saves the __dict__ to JSON"""
#  with open(filename, "w", encoding="utf-8") as bf:
#     JSON.dump(self.__dict__, bf)
