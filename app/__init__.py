"""This package contains all Flask information including routes and the
flask application"""
from flask import Flask

app = Flask(__name__)

from app import routes
