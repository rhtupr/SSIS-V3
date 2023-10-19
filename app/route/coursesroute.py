from flask import * 
from app.models.courses import *
from flask_wtf import *

courses_bp = Blueprint ('courses', __name__)

@courses_bp.route('/courses/')
def courses():
    courses = courseread()
    return render_template('courses.html', courses=courses)

@courses_bp.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        coursecode = request.form['coursecode']
        coursename = request.form['coursename']
        collegecode = request.form['collegecode']
        print(coursecode, coursename, collegecode)
        add_cou(coursecode, coursename, collegecode)
        return redirect('/courses')
    return render_template('courses.html')

@courses_bp.route('/courses/search', methods=['GET', 'POST'])
def search_courses():
    courses = []
    if request.method == 'POST':
        search_query = request.form.get('search_course')
        if search_query:
            courses = find_courses(search_query)
    return render_template('courses.html', courses=courses)

@courses_bp.route('/courses/delete/<string:coursecode>', methods=['DELETE'])
def remove_course(coursecode):
    if request.method == 'DELETE':
        print(coursecode)
        delete_course(coursecode)
        return jsonify({'success': True})



