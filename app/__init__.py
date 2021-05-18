"""This package contains all Flask information including routes and the
flask application"""
from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Contains flask application configure settings."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sec-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)

from app import routes
