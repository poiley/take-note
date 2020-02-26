from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from app.forms.lecture import AddLectureForm
from app.models.user import User
from app.models.lecture import Lecture
from app.models.site import Sidelink, Sidebar

blueprint = Blueprint('lecture', __name__, url_prefix='/lecture')

@login_required
@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddLectureForm(request.form)
    u = User.get(current_user.get_id())
    
    if request.method == 'POST' and form.validate():
        l = Lecture.query.filter_by(dept=form.dept) \
                         .filter_by(course_num=form.course_num) \
                         .filter_by(section=form.section).first()

        if l:
            u.lecture.append(l)

        return redirect(url_for('lecture.my', user=u, lectures=user.lecture))
       
    return render_template("lecture/add.html", sidelinks=sidelinks, sidebar=sidebar, user=u, form=form)

@login_required
@blueprint.route('/my', methods=['GET'])
def my():
    u = User.get(current_user.get_id())

    sidelinks = [Sidelink('Add A Lecture', 'lecture.add', 'Add a lecture to your schedule.')]
    sidebar   = [Sidebar('My Lectures', 'lecture.my'), Sidebar('Github', 'https://github.com/poiley/take-note', True)]
    return render_template("lecture/my.html", sidelinks=sidelinks, sidebar=sidebar, user=u, lectures=u.lecture)