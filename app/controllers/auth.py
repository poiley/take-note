import requests, urllib
from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from app.extensions import db, login_manager
from app.forms.auth import SigninForm, SignupForm
from app.models.user import User

blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@blueprint.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))

    form = SigninForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.data['username']).first()

        if not user or not user.check_password(form.data['password']):
            flash('Invalid Username or Password.')
            return redirect(url_for('auth.signin'))
        
        login_user(user, remember=True)
        
        return redirect(url_for('home.home'))

    return render_template('auth/signin.html', form=form)


@blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    
    if request.method == 'POST' and form.validate():
        user = User(form.data['username'], form.data['displayname'], generate_password_hash(form.data['password']))

        db.session.add(user)
        db.session.commit()

        login_user(user, remember=True)

        return redirect(url_for('lecture.my'))
       
    return render_template("auth/signup.html", form=form)

@blueprint.route("/signout")
@login_required
def signout():
    logout_user()
    return redirect(url_for('home.home'))

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
