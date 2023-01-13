#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function called with / route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function called with /hbnb route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_c(text):
    """Function called to return /c/<text> route"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_py(text='is cool'):
    """Function called to return /python/<text> route"""
    if text is not 'is cool':
        text = text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def text_nu(n):
    """Function called to return number"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_t(n):
    """function that returns a template with number"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
