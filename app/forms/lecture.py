from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class AddLectureForm(FlaskForm):
    dept       = StringField('Department', validators=[DataRequired(), Length(min=4, max=10)])
    course_num = StringField('Course Number', validators=[DataRequired(), Length(min=1, max=10)])
    section    = StringField('Section', validators=[DataRequired(), Length(min=1, max=8)])
    start      = StringField('Start Time', validators=[DataRequired(), Length(min=1, max=5)])
    end        = StringField('End Time', validators=[DataRequired(), Length(min=1, max=5)])
    hall       = StringField('Hall', validators=[DataRequired(), Length(min=1, max=50)])

class SearchForm(FlaskForm):
    dept       = StringField('Department', validators=[Length(min=0, max=10)])
    course_num = StringField('Course Number', validators=[Length(min=0, max=10)])
    title      = StringField('Course Title', validators=[Length(min=0, max=50)])