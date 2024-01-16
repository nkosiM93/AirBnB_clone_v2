#!/usr/bin/python

import unittest
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Tests the functionalitty of the different console methods"""

    def test_create(self):
        count = len(storage.all())
        HBNBCommand().do_create(
                        "Place city_id=\"0001\" user_id=\"0001\" "
                        "name=\"My_little_house\" "
                        "number_rooms=4 number_bathrooms=2 "
                        "max_guest=10 price_by_night=300 "
                        "latitude=37.773972 longitude=-122.431297")
        self.assertTrue(count < len(storage.all()))
