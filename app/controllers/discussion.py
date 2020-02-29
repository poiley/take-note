from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from app.models.user import User
from app.models.site import Sidelink, Sidebar
from app.models.lecture import Lecture

blueprint = Blueprint('discussion', __name__, url_prefix='/discussion')

@login_required
@blueprint.route('/board', methods=['GET', 'POST'])
def board():
    if not request.args.get('id'):
        return redirect(url_for('lecture.my'))
    
    lect = Lecture.query.filter_by(id=request.args.get('id')).first()
    
    if not lect:
        return redirect(url_for('lecture.my'))

    sidelinks = [Sidelink('My Lectures', 'lecture.my', 'View lectures.'), Sidelink('Chat', '#', 'Chat with classmates.', True), Sidelink('Notes', 'note.view', 'See the work classmates have shared.')]
    sidebar   = [Sidebar('My Lectures', 'lecture.my'), Sidebar('Github', 'https://github.com/poiley/take-note', True), Sidebar('Sign Out', 'auth.signout')]

    return render_template('discussion/board.html', lecture=lect, sidelinks=sidelinks, sidebar=sidebar)