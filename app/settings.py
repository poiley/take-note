"""Settings configuration - Configuration for environment variables can go in here."""

import os

SECRET_KEY = os.urandom(32)
ENV = os.getenv('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(os.path.realpath(__file__)), '../app.sqlite')