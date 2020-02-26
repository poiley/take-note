from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from app.models.user import User
from app.models.lecture import Lecture
from app.models.site import Sidelink, Sidebar

blueprint = Blueprint('home', __name__)

@blueprint.route('/', methods=['GET'])
def home():
    # Lecture.json_to_database()
    if current_user.is_authenticated:
        return redirect(url_for('lecture.my'))

    sidelinks   = [Sidelink('Sign In', 'auth.signin', 'sign in'), Sidelink('Sign Up', 'auth.signup', 'sign up') ]
    sidebar     = [Sidebar('Github', 'https://github.com/poiley/take-note', True)]
    return render_template('home/index.html', sidelinks=sidelinks, sidebar=sidebar)
    