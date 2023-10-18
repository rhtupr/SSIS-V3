from flask import * 
from app.models.courses import *
from flask_wtf import *

courses_bp = Blueprint ('courses', __name__)

@courses_bp.route('/courses/')
def courses():
    courses = courseread()
    return render_template('courses.html', courses=courses)