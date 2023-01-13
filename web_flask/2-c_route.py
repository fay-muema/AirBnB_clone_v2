#!/usr/bin/python3
from flask import Flask
"""flask which created two routes"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C %s' % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
