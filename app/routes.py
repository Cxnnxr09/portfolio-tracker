"""From app imports the flask application object and the flask
render_template functionality."""
from app import app
from flask import render_template, url_for, flash, redirect


@app.route('/')
@app.route('/home')
def home():
    """
    Return html or template and displays under the route.

    :return: template 'home.html'
    """
    return render_template('home.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Return html or template for page and form. If Form is completed returns
    redirect to home page.

    :return: template 'login.html'
    """
    return render_template('login.html', title="Login")


@app.route('/register', methods=['GET', 'POST'])
def register():
    pass


@app.route('/dashboard', methods=['GET', 'POST'])
def dshaboard():
    return render_template('dashboard.html', title='Dashboard')
