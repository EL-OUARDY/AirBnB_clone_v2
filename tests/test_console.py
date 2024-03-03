#!/usr/bin/python3
"""unittests for console.py"""
import unittest
from unittest.mock import patch
from io import StringIO

from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage
import os
from typing import TextIO
from models.user import User

import MySQLdb


class TestHBNBCommand(unittest.TestCase):
    """Tests HBNBCommand console interpreter class"""

    classes = storage.get_app_classes()

    @classmethod
    def setUpClass(cls):
        """Executes once before running tests"""
        # resets storage data
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            # remove json file
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Runs after each test"""
        # resets storage data
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            # remove json file
            os.remove(FileStorage._FileStorage__file_path)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db", "Only File Storage"
    )
    def test_fs_create(self):
        """tests create command - file storage."""
        with patch("sys.stdout", new=StringIO()) as f:
            cons = HBNBCommand()
            cons.onecmd('create City name="Zagora"')
            _id = f.getvalue().strip()
            self.clear_stream(f)
            self.assertIn(f"City.{_id}", storage.all().keys())
            cons.onecmd(f"show City {_id}")
            self.assertIn("'name': 'Zagora'", f.getvalue().strip())
            self.clear_stream(f)
            cons.onecmd('create User name="Ouadia" age=26')
            _id = f.getvalue().strip()
            self.assertIn(f"User.{_id}", storage.all().keys())
            self.clear_stream(f)
            cons.onecmd(f"show User {_id}")
            self.assertIn("'name': 'Ouadia'", f.getvalue().strip())
            self.assertIn("'age': 26", f.getvalue().strip())

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "Only DB Storage")
    def test_db_create(self):
        """tests create command - database storage."""
        with patch("sys.stdout", new=StringIO()) as f:
            cons = HBNBCommand()
            # create user object
            self.clear_stream(f)
            cons.onecmd(
                'create User email="ouadia@elouardy.com" password="pwd"'
            )
            _id = f.getvalue().strip()
            dbc = MySQLdb.connect(
                host=os.getenv("HBNB_MYSQL_HOST"),
                port=3306,
                user=os.getenv("HBNB_MYSQL_USER"),
                passwd=os.getenv("HBNB_MYSQL_PWD"),
                db=os.getenv("HBNB_MYSQL_DB"),
            )
            cursor = dbc.cursor()
            cursor.execute(f'SELECT * FROM users WHERE id="{_id}"')
            result = cursor.fetchone()
            self.assertTrue(result is not None)
            self.assertIn("ouadia@elouardy.com", result)
            self.assertIn("pwd", result)
            cursor.close()
            dbc.close()

    def clear_stream(self, stream: TextIO):
        """clear the content of a given stream"""
        if stream.seekable():
            stream.seek(0)
            stream.truncate(0)


if __name__ == "__main__":
    unittest.main()
