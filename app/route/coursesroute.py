from flask import * 
from app.models.courses import *
from flask_wtf import *

courses_bp = Blueprint ('courses', __name__)

@courses_bp.route('/courses/')
def courses():
    courses = courseread()
    return render_template('courses.html', courses=courses)

@courses_bp.route('/courses/', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        coursecode = request.form['coursecode']
        coursename = request.form['coursename']
        collegecode = request.form['collegecode']
        add_cou(coursecode, coursename, collegecode)
        return redirect('/courses')
    return render_template('courses.html')
