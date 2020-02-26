from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy import and_
from app.forms.lecture import AddLectureForm, SearchForm
from app.models.user import User
from app.models.lecture import Lecture
from app.models.site import Sidelink, Sidebar

blueprint = Blueprint('lecture', __name__, url_prefix='/lecture')

@login_required
@blueprint.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    
    if request.method == 'POST' and form.validate():
        results = Lecture.query.filter_by(dept=form.dept.data)

        if form.course_num.data is not '':
            results = results.filter_by(course_num=form.course_num.data)

        if form.title.data is not '':
            results = results.filter_by(title=form.title.data)

        if len(results.all()) == 0:
            return redirect(url_for('lecture.search'))
        elif len(results.all()) == 1:
            return redirect(url_for('lecture.add', lecture=results.all()[0].id))

        lecture_ids = []
        for result in results.all():
            lecture_ids.append(result.id)

        return search_results(lecture_ids)
       
    sidelinks = [Sidelink('Search', "javascript:document.getElementById('searchform').submit()", 'Submit query', True)]
    sidebar   = [Sidebar('My Lectures', 'lecture.my'), Sidebar('Github', 'https://github.com/poiley/take-note', True), Sidebar('Sign Out', 'auth.signout')]
    return render_template('lecture/search.html', sidelinks=sidelinks, sidebar=sidebar, form=form)

@login_required
@blueprint.route('/result')
def search_results(ids):
    results = []

    for i in ids:
        results.append(Lecture.get(i))

    sidelinks = [Sidelink('Add', "javascript:document.getElementById('addlecture').submit()", 'Add the selected lecture', True), Sidelink('Search Again', 'lecture.search', 'Try a different search')]
    sidebar   = [Sidebar('My Lectures', 'lecture.my'), Sidebar('Github', 'https://github.com/poiley/take-note', True), Sidebar('Sign Out', 'auth.signout')]
    return render_template('lecture/results.html', sidelinks=sidelinks, sidebar=sidebar, results=results)


@login_required
@blueprint.route('/add')
def add():
    return "hello world"


@login_required
@blueprint.route('/my', methods=['GET'])
def my():
    u = User.get(current_user.get_id())

    sidelinks = [Sidelink('Add A Lecture', 'lecture.search', 'Add a lecture to your schedule.')]
    sidebar   = [Sidebar('My Lectures', 'lecture.my'), Sidebar('Github', 'https://github.com/poiley/take-note', True), Sidebar('Sign Out', 'auth.signout')]
    return render_template('lecture/my.html', sidelinks=sidelinks, sidebar=sidebar, user=u, lectures=u.lecture)