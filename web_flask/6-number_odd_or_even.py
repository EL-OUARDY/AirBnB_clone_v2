#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n: int):
    """Display n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n: int):
    """Display a HTML page only if n is an integer"""
    return render_template("5-number.html", number=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n: int):
    """Display a HTML page only if n is an integer"""
    return render_template("6-number_odd_or_even.html", number=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
