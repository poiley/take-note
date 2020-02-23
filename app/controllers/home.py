from flask import Blueprint, render_template
from flask_login import current_user
from app.models.user import User

blueprint = Blueprint('home', __name__)

@blueprint.route('/', methods=['GET'])
def home():
    if not current_user.is_authenticated:
        return render_template('home/index_notauth.html')

    user = User.get(current_user.get_id())

    return render_template('home/index_auth.html', current_user=current_user)
