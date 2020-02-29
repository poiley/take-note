from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy import and_
from app.forms.lecture import AddLectureForm, SearchForm
from app.models.user import User
from app.models.lecture import Lecture
from app.models.hall import Hall
from app.models.site import Sidelink, Sidebar
from app.extensions import db
from app.services.location import get_halls, get_distance
from app.services.schedule import get_weekday_letter
import time
from datetime import datetime
import numpy

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
            return redirect(url_for('lecture.add', id=[results.all()[0].id]))

        lecture_ids = []
        for result in results.all():
            lecture_ids.append(result.id)

        return search_results(lecture_ids)
       
    sidelinks = [Sidelink('Search', "javascript:document.getElementById('searchform').submit()", 'Submit query', True), Sidelink('Locate', "lecture.locate", 'Get a list of classes currently in session near you')]
    sidebar   = [Sidebar('My Lectures', 'lecture.my'), Sidebar('Github', 'https://github.com/poiley/take-note', True), Sidebar('Sign Out', 'auth.signout')]
    return render_template('lecture/search.html', sidelinks=sidelinks, sidebar=sidebar, form=form)

@login_required
@blueprint.route('/result')
def search_results(ids):
    results = []
    for i in ids:
        results.append(Lecture.get(i))

    sidelinks = [Sidelink('Add', '#', 'Add the selected lecture', True, css_classes='sidelink add', onclick="addClass()"), Sidelink('Search Again', 'lecture.search', 'Try a different search')]
    sidebar   = [Sidebar('My Lectures', 'lecture.my'), Sidebar('Github', 'https://github.com/poiley/take-note', True), Sidebar('Sign Out', 'auth.signout')]
    return render_template('lecture/results.html', sidelinks=sidelinks, sidebar=sidebar, results=results)


@login_required
@blueprint.route('/add')
def add():
    lect = Lecture.get(request.args.get('id'))
    user = User.get(current_user.get_id())

    user.lecture.append(lect)

    db.session.commit()

    return redirect(url_for('lecture.my'))


@login_required
@blueprint.route('/my')
def my():
    u = User.get(current_user.get_id())

    sidelinks = [Sidelink('Add A Lecture', 'lecture.search', 'Add a lecture to your schedule.'), Sidelink('View Class', '#', 'View the selected lecture.', True, onclick="viewClass()")]
    sidebar   = [Sidebar('My Lectures', 'lecture.my'), Sidebar('Github', 'https://github.com/poiley/take-note', True), Sidebar('Sign Out', 'auth.signout')]
    return render_template('lecture/my.html', sidelinks=sidelinks, sidebar=sidebar, user=u, lectures=u.lecture)


@login_required
@blueprint.route('/locate')
def locate():
    if request.args.get('x') != None and request.args.get('y') != None:
        current_location = (request.args.get('x'), request.args.get('y'))
        halls = Hall.query.all()

        closest_hall = halls[0]

        hall_distance_map = []
        for hall in halls:
            hall_distance_map.append((hall, get_distance(hall, current_location)))

        hall_distance_map = [item for item in hall_distance_map if item[1] < 100]
        hall_distance_map_sorted = sorted(hall_distance_map, key=lambda x: x[1])

        sd = numpy.array([hall[1] for hall in hall_distance_map_sorted]).std()

        less_than_five_stddev = [item for item in hall_distance_map_sorted if (item[1]/sd) * 100 <= 5]

        return match([int(i[0].id) for i in less_than_five_stddev])
    else:
        return render_template('lecture/location.html')

@login_required
@blueprint.route('/match')
def match(ids):
    if not ids:
        return redirect(url_for('lecture.my'))

    nearby_halls          = [Hall.query.filter_by(id=ids[0]).first()]
    for i in range(1, len(ids)):
        nearby_halls.append(Hall.query.filter_by(id=ids[i]).first())

    lectures_filtered_ids = []
    now                   = datetime.now()
    for h in nearby_halls:
        for lecture in Lecture.query.filter_by(hall_id=h.id).all():
            if lecture.start == 'Online':
                continue
            
            start_time = convert_string_to_time(lecture.start)
            end_time   = convert_string_to_time(lecture.end)

            if now.time() >= start_time.time() and now.time() <= end_time.time():
                    if get_weekday_letter().lower() in lecture.days.lower():
                        lectures_filtered_ids.append(lecture.id)

    return search_results(lectures_filtered_ids)

def convert_string_to_time(input):
    if '.' in str(input):
        if len(str(input).split('.')[1]) == 1:
            return datetime.strptime(str(input) + '0', "%H.%M")
        else:
            return datetime.strptime(str(input), "%H.%M")
    else:
        return datetime.strptime(str(input), "%H")