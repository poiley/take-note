from flask import Blueprint, render_template
from flask_login import current_user
from app.models.user import User

blueprint = Blueprint('home', __name__)

@blueprint.route('/', methods=['GET'])
def home():
    if not current_user.is_authenticated:
        return render_template('home/index_auth.html')

    user = User.get(current_user.get_id())

    user.update_token(spotify_handler.refresh_access_token(user.refresh_token))

    return render_template('home/index_noauth.html', current_user=current_user)
