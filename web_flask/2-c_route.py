#!/usr/bin/python3
""" Flask web application.

Listens on 0.0.0.0, port 5000.
Routes:
    /: Print'Hello HBNB!'.
    /hbnb: Print'HBNB'.
    /c/<text>: Print 'C' then the value of <text>.
"""
from flask import Flask

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
    """Prints 'C' and the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
