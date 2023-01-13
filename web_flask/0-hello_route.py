#!/usr/bin/python3
""" Script for running flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function called with route function"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
