#!/usr/bin/python3
""" test state """
import os

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv("HBNB_TYPE_STORAGE") != "db" else type(None),
        )
