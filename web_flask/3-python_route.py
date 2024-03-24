#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    """Return a greet string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return HBNB string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_lang(text: str):
    """Return C letter followed by passed parameter"""
    return f'C {text.replace("_", " ")}'


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text: str = "is cool"):
    """Return “Python” string followed by passed parameter/default"""
    return f'Python {text.replace("_", " ")}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
