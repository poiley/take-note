"""Settings configuration - Configuration for environment variables can go in here."""

import os

ENV = os.getenv('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(os.path.realpath(__file__)), '../app.sqlite')
#SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')