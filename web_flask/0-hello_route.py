#!/usr/bin/python3
"""This app starts a Flask web application.
Listens on 0.0.0.0, port 5000.
Routes:
    /: Print 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Print 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
