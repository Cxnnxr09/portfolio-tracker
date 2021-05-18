"""From app imports the flask application object and the flask
render_template functionality."""
from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm


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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    pass


@app.route('/dashboard', methods=['GET', 'POST'])
def dshaboard():
    return render_template('dashboard.html', title='Dashboard')