#!/usr/bin/python3
from flask import Flask
"""flask which created two routes"""

app = Flask(__name__)

@app.route('/', strict_slashes=False)


def hello():
    """function too print hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)


def hbnb():
    """second function"""
    return 'HBNB'

@app.route('/c', strict_slashes=False)
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    

    return render_template('index.html', processed_text=processed_text)
if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")

