"""Extensions module - Set up for additional libraries can go in here."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask_login import LoginManager

db = SQLAlchemy()

Base = declarative_base()

login_manager = LoginManager()