#!/usr/bin/python3
""" Flask web application.

Listens on 0.0.0.0, port 5000.
Routes:
    /: Print 'Hello HBNB!'.
    /hbnb: Print 'HBNB'.
    /c/<text>: Print 'C' followed by the value of <text>.
    /python/(<text>): Print 'Python' followed by the value of <text>.
    /number/<n>: Print 'n is a number' only if <n> is an integer.
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Print 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Print 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Print 'C' followed by the value of <text>.

    Replace underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Print 'Python' followed by the value of <text>.

    Replace underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Print 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
