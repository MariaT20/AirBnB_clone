#!/usr/bin/python3
"""This module contains ClassLoader class"""

import os
from pathlib import Path
from importlib import import_module


class ClassLoader:
    """Defines a `load` method which loads a given class from `models`"""

    __classes = {}

    @classmethod
    def load(cls, name=""):
        """Loads a given class.

        Args:
            name(str): The name of the class to be loaded
        """

        if type(name) is not str:
            return None

        # load class from __classes (caching)
        obj_cls = cls.__classes.get(name, None)
        if obj_cls is not None:
            return obj_cls

        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = Path(current_dir).parent.absolute()
        models_dir = "{}/models".format(parent_dir)

        for filename in os.listdir(models_dir):
            if (not filename.startswith("__")):
                # Remove extension from filename
                module_name = filename.split(".")[0]
                # Load module
                module = import_module("models.{}".format(module_name))
                try:
                    # Check if module has this class
                    cls.__classes[name] = getattr(module, name)
                    return cls.__classes[name]
                except AttributeError as ex:
                    # Fail silently
                    pass
        return None
