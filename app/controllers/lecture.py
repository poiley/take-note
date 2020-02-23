from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from app.forms.lecture import AddLectureForm
from app.models.user import User
from app.models.lecture import Lecture

blueprint = Blueprint('lecture', __name__, url_prefix='/lecture')

@login_required
@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddLectureForm(request.form)
    
    if request.method == 'POST' and form.validate():
        user = User.get(current_user.get_id())
        
        lect = Lecture.query.filter_by(dept=form.dept) \
                            .filter_by(course_num=form.course_num) \
                            .filter_by(section=form.section).first()

        if lect:
            user.lecture.append(lect)

        return redirect(url_for('lecture.my', user=user, lectures=user.lecture))
       
    render_template("lecture/add.html", user=user, form=form)

@login_required
@blueprint.route('/my', methods=['GET'])
def my():
    user = User.get(current_user.get_id())
    render_template("lecture/my.html", user=user lectures=user.lecture)