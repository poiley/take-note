from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models.user import User

class SignupForm(FlaskForm):
    username    = StringField('Username', validators=[DataRequired(), Length(min=4, max=32)])
    displayname = StringField('Display Name', validators=[DataRequired(), Length(min=1, max=32)])
    password    = PasswordField('Password', validators=[DataRequired()])

    def validate_username(self, username):
        if not username.data:
            raise ValidationError('Please enter a username.')
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('That username is taken. Please choose another.')
        if len(username.data) > 32:
            raise ValidationError('That username is too long. Please enter another.')

class SigninForm(FlaskForm):
    username    = StringField('Username', validators=[DataRequired(), Length(min=4, max=32)])                           
    password    = PasswordField('Password', validators=[DataRequired()])

    def validate_username(self, username):
        if not username.data:
            raise ValidationError('Please enter a username.')
        if len(username.data) > 32:
            raise ValidationError('That username is too long. Please try again.')