from flask import Blueprint, render_template
from flask_login import current_user
from app.models.user import User

blueprint = Blueprint('lecture', __name__, url_prefix='/lecture')

@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    render_template("lecture/add.html")

@blueprint.route('/my', methods=['GET'])
def my():
    render_template("lecture/my.html")