#!/usr/bin/python3
""" Module for testing database storage"""

import datetime
import unittest

import MySQLdb
from models.base_model import BaseModel
from models import storage
import os

from models.user import User


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "Only DB_Storage")
class TestDBStorage(unittest.TestCase):
    """test database storage engine"""

    def test_save(self):
        """test saving new records"""

        # get the total count of users before adding new record
        count_before = self.get_users_total_count()

        # add new record
        new_user = User(
            **{
                "first_name": "Xouadia",
                "last_name": "elouardy",
                "email": "ouadia@elouardy.com",
                "password": 123,
            }
        )
        new_user.save()

        # get the total count of users after adding new record
        count_after = self.get_users_total_count()

        # check if record added successfuly
        self.assertEqual((count_before + 1), count_after)

    def get_users_total_count(self):
        db = MySQLdb.connect(
            user=os.getenv("HBNB_MYSQL_USER"),
            host=os.getenv("HBNB_MYSQL_HOST"),
            passwd=os.getenv("HBNB_MYSQL_PWD"),
            port=3306,
            db=os.getenv("HBNB_MYSQL_DB"),
        )
        cur = db.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        count = cur.fetchone()[0]
        cur.close()
        db.close()

        return count
