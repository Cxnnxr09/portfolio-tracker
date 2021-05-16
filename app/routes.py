"""From app imports the flask application object and the flask
render_template functionality."""
from app import app
from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    """
Return html or template and displays under the route.

    :return: template 'home.html'
    """
    return render_template('home.html', title="Home")
