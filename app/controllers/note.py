from flask import Blueprint, render_template
from flask_login import current_user
from app.models.user import User

blueprint = Blueprint('note', __name__, url_prefix='/note')

@blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
    render_template("upload.html")

@blueprint.route('/view', methods=['GET'])
def view():
    render_template("view.html")