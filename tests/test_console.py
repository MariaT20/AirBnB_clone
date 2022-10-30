#!/usr/bin/python3
"""Contains all test cases of HBNBCommand console"""

import re
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    """defines test cases for HBNBCommand"""

    def test_do_count(self):
        """It should return instance count of BaseModel
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count_user(self):
        """It should return instance count of User
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count_place(self):
        """It should return instance count of Place
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Place")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count_amenity(self):
        """It should return instance count of Amenity
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Amenity")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count_city(self):
        """It should return instance count of City
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count City")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count_review(self):
        """It should return instance count of Review
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Review")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count_state(self):
        """It should return instance count of State
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do__count_user(self):
        """It should return instance count of User
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count__place(self):
        """It should return instance count of Place
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count__amenity(self):
        """It should return instance count of Amenity
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count__city(self):
        """It should return instance count of City
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count__review(self):
        """It should return instance count of Review
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count__state(self):
        """It should return instance count of State
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count_missing_class(self):
        """It should fail to count
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_count_class_not_exists(self):
        """It should fail to count
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_count__class_not_exists(self):
        """It should fail to count
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_create(self):
        """It should create a BaseModel using `create BaseModel` cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            key = "BaseModel.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, BaseModel)

    def test_do_create_user(self):
        """It should create a User using User.create() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, User)

    def test_do__create(self):
        """It should create a BaseModel using `BaseModel.create()` cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
            obj_id = f.getvalue().strip()
            key = "BaseModel.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, BaseModel)

    def test_do_create_place(self):
        """It should create a Place using create Place cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            obj_id = f.getvalue().strip()
            key = "Place.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, Place)

    def test_do_create_amenity(self):
        """It should create a Amenity using create Amenity cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            obj_id = f.getvalue().strip()
            key = "Amenity.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, Amenity)

    def test_do_create_city(self):
        """It should create a City using create City cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            obj_id = f.getvalue().strip()
            key = "City.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, City)

    def test_do_create_review(self):
        """It should create a Review using create Review cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            obj_id = f.getvalue().strip()
            key = "Review.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, Review)

    def test_do_create_state(self):
        """It should create a State using create State cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            obj_id = f.getvalue().strip()
            key = "State.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, State)

    def test_do_create__user(self):
        """It should create a User using User.create() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, User)

    def test_do_create__place(self):
        """It should create a Place using Place.create() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
            obj_id = f.getvalue().strip()
            key = "Place.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, Place)

    def test_do_create__amenity(self):
        """It should create a Amenity using Amenity.create() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
            obj_id = f.getvalue().strip()
            key = "Amenity.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, Amenity)

    def test_do_create__city(self):
        """It should create a City using City.create() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
            obj_id = f.getvalue().strip()
            key = "City.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, City)

    def test_do_create__review(self):
        """It should create a Review using Review.create() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
            obj_id = f.getvalue().strip()
            key = "Review.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, Review)

    def test_do_create__state(self):
        """It should create a State using State.create() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
            obj_id = f.getvalue().strip()
            key = "State.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, State)

    def test_do_create_missing_class(self):
        """It should fail to create
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            msg = f.getvalue().strip()
            self.assertEqual(msg, "** class name missing **")

    def test_do_create_class_not_exists(self):
        """It should fail to create MyModel
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            msg = f.getvalue().strip()
            self.assertEqual(msg, "** class doesn't exist **")

    def test_do_create_user(self):
        """It should create a User using User.create() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, User)

    def test_do_create_model_not_exists(self):
        """It should fail to create MyModel
        MyModel.create()
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.create()")
            msg = f.getvalue().strip()
            self.assertEqual(msg, "** class doesn't exist **")

    def test_do_all(self):
        """It should display only BaseModel instances using
        cmd all BaseModel
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"Place", output)
            self.assertIsNone(match)

    def test_do_all_users(self):
        """It should display only User instances using
        cmd all User
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"Place", output)
            self.assertIsNone(match)

    def test_do_all_places(self):
        """It should display only Place instances using
        cmd all Place
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Place")

            HBNBCommand().onecmd("all Place")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"User", output)
            self.assertIsNone(match)

    def test_do_all_amenities(self):
        """It should display only Amenity instances using
        cmd all Amenity
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Amenity")

            HBNBCommand().onecmd("all Amenity")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"User", output)
            self.assertIsNone(match)

    def test_do_all_reviews(self):
        """It should display only Review instances using
        cmd all Review
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Review")

            HBNBCommand().onecmd("all Review")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"User", output)
            self.assertIsNone(match)

    def test_do_all_states(self):
        """It should display only State instances using
        cmd all State
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create State")

            HBNBCommand().onecmd("all State")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"User", output)
            self.assertIsNone(match)

    def test_do_all_cities(self):
        """It should display only City instances using
        cmd all City
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create City")

            HBNBCommand().onecmd("all City")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"User", output)
            self.assertIsNone(match)

    def test_do_all_(self):
        """It should display only BaseModel instances using
        cmd all BaseModel
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("BaseModel.all()")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"Place", output)
            self.assertIsNone(match)

    def test_do_all__users(self):
        """It should display only User instances using
        cmd User.all()
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("User.all")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"Place", output)
            self.assertIsNone(match)

    def test_do_all__places(self):
        """It should display only Place instances using
        cmd Place.all()
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Place")

            HBNBCommand().onecmd("Place.all()")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"User", output)
            self.assertIsNone(match)

    def test_do_all__amenities(self):
        """It should display only Amenity instances using
        cmd Amenity.all()
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Amenity")

            HBNBCommand().onecmd("Amenity.all()")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"User", output)
            self.assertIsNone(match)

    def test_do_all__reviews(self):
        """It should display only Review instances using
        cmd Review.all()
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Review")

            HBNBCommand().onecmd("Review.all()")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"User", output)
            self.assertIsNone(match)

    def test_do_all__states(self):
        """It should display only State instances using
        cmd State.all()
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create State")

            HBNBCommand().onecmd("State.all()")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"User", output)
            self.assertIsNone(match)

    def test_do_all__cities(self):
        """It should display only City instances using
        cmd City.all()
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create City")

            HBNBCommand().onecmd("City.all()")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"User", output)
            self.assertIsNone(match)

    def test_do_all_class_not_exists(self):
        """It should fail to display MyModel
        instances
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_all__class_not_exists(self):
        """It should fail to display MyModel
        instances
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.all()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_show(self):
        """It should display a BaseModel with given id using
        show BaseModel id cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("show BaseModel {}".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "BaseModel.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show_user(self):
        """It should display a User with given id using
        show User id cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("show User {}".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "User.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show_place(self):
        """It should display a Place with given id using
        show Place id cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("show Place {}".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "Place.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show_review(self):
        """It should display a Review with given id using
        show Review id cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("show Review {}".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "Review.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show_amenity(self):
        """It should display a Amenity with given id using
        show Amenity id cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("show Amenity {}".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "Amenity.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show_city(self):
        """It should display a City with given id using
        show City id cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("show City {}".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "City.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show_state(self):
        """It should display a State with given id using
        show State id cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("show State {}".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "State.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do__show(self):
        """It should display a BaseModel with given id using
        BaseModel.show(id) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("BaseModel.show({})".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "BaseModel.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show__user(self):
        """It should display a User with given id using
        User.show(id) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("show User {}".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "User.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show__place(self):
        """It should display a Place with given id using
        Place.show(id) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("Place.show({})".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "Place.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show__review(self):
        """It should display a Review with given id using
        Review.show(id) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("Review.show({})".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "Review.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show__amenity(self):
        """It should display a Amenity with given id using
        Amenity.show(id) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("Amenity.show({})".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "Amenity.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show__city(self):
        """It should display a City with given id using
        City.show(id) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("City.show({})".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "City.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show__state(self):
        """It should display a State with given id using
        State.show(id) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("State.show({})".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            key = "State.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertEqual(len(str(obj)), len(output))

    def test_do_show_missing_class(self):
        """It should fail to show
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_show_class_not_exists(self):
        """It should fail to show MyModel
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do__show_class_not_exists(self):
        """It should fail to MyModel.show()
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.show()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_show_missing_id(self):
        """It should fail to show User with missing id
        using show User cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_show_user_missing_id(self):
        """It should fail to show User with missing id
        using User.show() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_show_user_invalid_id(self):
        """It should fail to show User with invalid id
        using show User "test-1234" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User "test-1234"')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_show__user_invalid_id(self):
        """It should fail to show User with invalid id
        using User.show("test-1234") cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.show("test-1234")')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_update(self):
        """It should update BaseModel using
        update BaseModel id "attribute" "value" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "BaseModel"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'update BaseModel {} "first_name" "Betty"'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_user(self):
        """It should update User using
        update User id "attribute" "value" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "User"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'update User {} "first_name" "Betty"'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_place(self):
        """It should update Place using
        update Place id "attribute" "value" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Place"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'update Place {} "name" "Nigeria"'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_city(self):
        """It should update City using
        update City id "attribute" "value" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "City"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'update City {} "name" "Banana Island"'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_state(self):
        """It should update State using
        update State id "attribute" "value" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "State"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'update State {} "name" "Lagos"'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_review(self):
        """It should update Review using
        update Review id "attribute" "value" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Review"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'update Review {} "text" "nice"'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_amenity(self):
        """It should update Amenity using
        update Amenity id "attribute" "value" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Amenity"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'update Amenity {} "name" "swimming pool"'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update(self):
        """It should update BaseModel using
        BaseModel.update(id, "attribute", "value") cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "BaseModel"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'BaseModel.update("{}", "first_name", "Betty")'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_user(self):
        """It should update User using
        User.update(id, "attribute", "value") cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "User"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'User.update("{}", "first_name", "Betty")'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_place(self):
        """It should update Place using
        Place.update(id, "attribute", "value")
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Place"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'Place.update("{}", "name", "Nigeria")'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_city(self):
        """It should update City using
        City.update(id, "attribute", "value")
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "City"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'City.update("{}", "name", "Banana Island")'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update__state(self):
        """It should update State using
        State.update(id, "attribute", "value")
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "State"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'State.update("{}", "name", "Lagos")'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_review(self):
        """It should update Review using
        Review.update(id, "attribute", "value")
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Review"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'Review.update("{}", "text", "nice")'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update__amenity(self):
        """It should update Amenity using
        Amenity.update(id, "attribute", "value")
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Amenity"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'Amenity.update("{}", "name", "swimming pool",)'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_base_model_dict(self):
        """It should update with dict using
        BaseModel.update("id", {"first_name": "Betty"}) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "BaseModel"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            data = '{"first_name": "Betty"}'
            cmd = 'BaseModel.update("{}", {})'
            HBNBCommand().onecmd(cmd.format(obj_id, data))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_user_dict(self):
        """It should update with dict using
        User.update("id", {"first_name": "Betty"}) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "User"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            data = '{"first_name": "Betty"}'
            cmd = 'User.update("{}", {})'
            HBNBCommand().onecmd(cmd.format(obj_id, data))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_plcase_dict(self):
        """It should update with dict using
        Place.update("id", {"name": "Nigeria"}) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Place"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            data = '{"name": "Nigeria"}'
            cmd = 'Place.update("{}", {})'
            HBNBCommand().onecmd(cmd.format(obj_id, data))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_state_dict(self):
        """It should update with dict using
        State.update("id", {"name": "Lagos"}) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "State"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            data = '{"name": "Lagos"}'
            cmd = 'State.update("{}", {})'
            HBNBCommand().onecmd(cmd.format(obj_id, data))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_user_dict(self):
        """It should update with dict using
        City.update("id", {"name": "Surulere"}) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "City"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            data = '{"name": "Surulere"}'
            cmd = 'City.update("{}", {})'
            HBNBCommand().onecmd(cmd.format(obj_id, data))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_review_dict(self):
        """It should update with dict using
        Review.update("id", {"text": "nice place"}) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Review"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            data = '{"text": "nice place"}'
            cmd = 'Review.update("{}", {})'
            HBNBCommand().onecmd(cmd.format(obj_id, data))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_amenity_dict(self):
        """It should update with dict using
        Amenity.update("id", {"name": "spa"}) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Amenity"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            key = "{}.{}".format(model, obj_id)
            before_update = str(storage.all().get(key))
            data = '{"name": "spa"}'
            cmd = 'Amenity.update("{}", {})'
            HBNBCommand().onecmd(cmd.format(obj_id, data))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_missing_class(self):
        """It should fail to update using cmd
        update
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_do_update_class_not_exists(self):
        """It should fail to update using cmd
        update MyModel
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_do_update_id_missing(self):
        """It should fail to update using cmd
        update BaseModel
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update_user_id_missing(self):
        """It should fail to update using cmd
        update User
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update_place_id_missing(self):
        """It should fail to update using cmd
        update Place
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update Place")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update_state_id_missing(self):
        """It should fail to update using cmd
        update State
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update State")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update_city_id_missing(self):
        """It should fail to update using cmd
        update City
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update City")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update_amenity_id_missing(self):
        """It should fail to update using cmd
        update Amenity
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update Amenity")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update_review_id_missing(self):
        """It should fail to update using cmd
        update Review
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update Review")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update__id_missing(self):
        """It should fail to update using cmd
        BaseModel.update()
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("BaseModel.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update__user_id_missing(self):
        """It should fail to update using cmd
        User.update()
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("User.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update__place_id_missing(self):
        """It should fail to update using cmd
        Place.update()
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("Place.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update__state_id_missing(self):
        """It should fail to update using cmd
        State.update()
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("State.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update__city_id_missing(self):
        """It should fail to update using cmd
        City.update()
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("City.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update__amenity_id_missing(self):
        """It should fail to update using cmd
        Amenity.update()
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("Amenity.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update__review_id_missing(self):
        """It should fail to update using cmd
        Review.update()
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("Review.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update_no_attribute(self):
        """It should fail to update using cmd
        update User id
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("update User {}".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** attribute name missing **")

    def test_do_update_no_value(self):
        """It should fail to update using cmd
        update User id
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            command = 'update User {} "first_name"'
            HBNBCommand().onecmd(command.format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** value missing **")

    def test_do_update_user(self):
        """It should update User first_name using
        User.update("id", "first_name", "Betty") cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'User.update({}, "first_name", "Betty")'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_model_not_exists(self):
        """It should fail to update using cmd
        MyModel.update()
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("MyModel.update()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_do_update_user_missing_id(self):
        """It should fail to update using cmd
        User.update()
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("User.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update_user_invalid_id(self):
        """It should fail to update using cmd
        update User "test-1234"
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd('update User "test-1234"')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_do_update__user_invalid_id(self):
        """It should fail to update using cmd
        User.update("test-1234")
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd('User.update("test-1234")')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_do_update_user_missing_attribute(self):
        """It should fail to update using cmd
        User.update(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd('User.update("{}")'.format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** attribute name missing **")

    def test_do_update_user_missing_value(self):
        """It should fail to update using cmd
        User.update(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            command = 'User.update({}, "first_name")'
            HBNBCommand().onecmd(command.format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** value missing **")

    def test_do_update_user_empty_dict(self):
        """It should not have any effect on user using
        User.update(id, {})
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            before_update = str(storage.all().get(key))
            data = '{}'
            cmd = 'User.update("{}", {})'
            HBNBCommand().onecmd(cmd.format(obj_id, data))
            after_update = str(storage.all().get(key))
            self.assertEqual(before_update, after_update)

    def test_do_destroy(self):
        """It should delete an instance using the cmd
        destroy BaseModel id
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "BaseModel"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("destroy BaseModel {}".format(obj_id))
            HBNBCommand().onecmd("show {} {}".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_user(self):
        """It should delete an instance using the cmd
        destroy User id
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "User"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("destroy User {}".format(obj_id))
            HBNBCommand().onecmd("show {} {}".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_place(self):
        """It should delete an instance using the cmd
        destroy Place id
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Place"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("destroy Place {}".format(obj_id))
            HBNBCommand().onecmd("show {} {}".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_state(self):
        """It should delete an instance using the cmd
        destroy State id
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "State"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("destroy State {}".format(obj_id))
            HBNBCommand().onecmd("show {} {}".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_city(self):
        """It should delete an instance using the cmd
        destroy City id
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "City"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("destroy City {}".format(obj_id))
            HBNBCommand().onecmd("show {} {}".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_amenity(self):
        """It should delete an instance using the cmd
        destroy Amenity id
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Amenity"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("destroy Amenity {}".format(obj_id))
            HBNBCommand().onecmd("show {} {}".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_review(self):
        """It should delete an instance using the cmd
        destroy Review id
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Review"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("destroy Review {}".format(obj_id))
            HBNBCommand().onecmd("show {} {}".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_base_model(self):
        """It should delete an instance using the cmd
        BaseModel.destroy(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "BaseModel"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("BaseModel.destroy({})".format(obj_id))
            HBNBCommand().onecmd("{}.show({})".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy__user(self):
        """It should delete an instance using the cmd
        User.destroy(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "User"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("User.destroy({})".format(obj_id))
            HBNBCommand().onecmd("{}.show({})".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy__place(self):
        """It should delete an instance using the cmd
        Place.destroy(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Place"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("Place.destroy({})".format(obj_id))
            HBNBCommand().onecmd("{}.show({})".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy__state(self):
        """It should delete an instance using the cmd
        State.destroy(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "State"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("State.destroy({})".format(obj_id))
            HBNBCommand().onecmd("{}.show({})".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy__city(self):
        """It should delete an instance using the cmd
        City.destroy(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "City"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("City.destroy({})".format(obj_id))
            HBNBCommand().onecmd("{}.show({})".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy__amenity(self):
        """It should delete an instance using the cmd
        Amenity.destroy(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Amenity"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("Amenity.destroy({})".format(obj_id))
            HBNBCommand().onecmd("{}.show({})".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy__review(self):
        """It should delete an instance using the cmd
        Review.destroy(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:
            model = "Review"
            HBNBCommand().onecmd("create {}".format(model))
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("Review.destroy({})".format(obj_id))
            HBNBCommand().onecmd("{}.show({})".format(model, obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_missing_class(self):
        """It should fail to destroy
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_destroy_class_not_exists(self):
        """It should fail to destroy MyModel
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_destroy_missing_id(self):
        """It should fail to destroy User with missing id
        using destroy User cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_destroy_user_missing_id(self):
        """It should fail to destroy User with missing id
        using User.destroy() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_destroy_user_invalid_id(self):
        """It should fail to destroy User with missing id
        using destroy User "test-1234" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy User "test-1234"')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy__user_invalid_id(self):
        """It should fail to destroy User with missing id
        using User.destroy("test-1234") cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.destroy("test-1234")')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


if __name__ == "__main__":
    unittest.main(TestHBNBCommand)
