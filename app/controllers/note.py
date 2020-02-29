from flask import Blueprint, render_template
from flask_login import current_user, login_required
from app.models.user import User
from app.models.site import Sidelink, Sidebar

blueprint = Blueprint('note', __name__, url_prefix='/note')

@blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
    sidelinks = [Sidelink('My Lectures', 'lecture.my', 'View lectures.'), Sidelink('Notes', 'note.view', 'See the work classmates have shared.'), Sidelink('Chat', 'discussion.board', 'Chat with classmates.')]
    sidebar   = [Sidebar('My Lectures', 'lecture.my'), Sidebar('Github', 'https://github.com/poiley/take-note', True), Sidebar('Sign Out', 'auth.signout')]
    return render_template('note/upload.html', sidelinks=sidelinks, sidebar=sidebar)

@blueprint.route('/view', methods=['GET'])
def view():
    sidelinks = [Sidelink('My Lectures', 'lecture.my', 'View lectures.'), Sidelink('Upload', 'note.upload', 'Upload notes.'), Sidelink('Chat', 'discussion.board', 'Chat with classmates.')]
    sidebar   = [Sidebar('My Lectures', 'lecture.my'), Sidebar('Github', 'https://github.com/poiley/take-note', True), Sidebar('Sign Out', 'auth.signout')]
    return render_template('note/view.html', sidelinks=sidelinks, sidebar=sidebar)