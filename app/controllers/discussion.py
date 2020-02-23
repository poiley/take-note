from flask import Blueprint, render_template
from flask_login import current_user
from app.models.user import User

blueprint = Blueprint('discussion', __name__, url_prefix='/discussion')

@blueprint.route('/', methods=['GET', 'POST'])
def board():
    render_template("discussion/board.html")