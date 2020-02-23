from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class AddLectureForm(FlaskForm):
    dept       = StringField('Username', validators=[DataRequired(), Length(min=4, max=32)])
    course_num = StringField('Display Name', validators=[DataRequired(), Length(min=1, max=32)])
    section    = StringField('Section', validators=[DataRequired(), Length(min=1, max=8)])
    start      = StringField('Section', validators=[DataRequired(), Length(min=1, max=5)])
    end        = StringField('Section', validators=[DataRequired(), Length(min=1, max=5)])
    hall       = StringField('Section', validators=[DataRequired(), Length(min=1, max=50)])