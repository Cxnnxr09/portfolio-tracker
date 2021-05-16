"""This package contains all Flask information including routes and the
flask application"""
from flask import Flask
import os


class Config(object):
    """Contains application configure information such as security key."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sec-key'


app = Flask(__name__)
app.config.from_object(Config)

from app import routes
