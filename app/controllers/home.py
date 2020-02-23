from flask import Blueprint, render_template
from flask_login import current_user
from app.models.user import User

blueprint = Blueprint('home', __name__)

@blueprint.route('/', methods=['GET'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('lecture.my'))
        # return render_template('home/index_auth.html', current_user=current_user)
   
    return render_template('home/index_notauth.html')