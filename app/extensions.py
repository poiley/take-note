"""Extensions module - Set up for additional libraries can go in here."""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CsrfProtect

db = SQLAlchemy()

login_manager = LoginManager()

csrf = CsrfProtect()