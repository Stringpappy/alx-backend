#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)

@app.route('/')
def index():
    """index page"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
