#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a HTML page that contains list of states"""
    states = storage.all("State")
    return render_template("7-states_list.html", states_list=states)


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy Sessionn after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
