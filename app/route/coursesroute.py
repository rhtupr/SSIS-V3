from flask import *
from app.models.courses import *
from flask_wtf import *

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses/')
def courses():
    courses = courseread()
    colleges = get_college()
    return render_template('courses.html', courses=courses, colleges=colleges)

@courses_bp.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        coursecode = request.form['coursecode']
        coursename = request.form['coursename']
        collegecode = request.form['collegecode']
        add_cou(coursecode, coursename, collegecode)
        return redirect('/courses')  # Redirect after processing the form data
    else:
        # Handle the GET request to display the form
        colleges = get_college()  # Get the college data here
        return render_template('addcourse.html', colleges=colleges)  # Pass 'colleges' to the template

@courses_bp.route('/courses/edit', methods=['GET', 'POST'])
def edit_course():
    if request.method == 'POST':
        course_code = request.form.get('course_code')
        new_course_name = request.form.get('course_name')
        new_college_code = request.form.get('college_code').upper()
        
        # Update the course information in the database
        update_course(course_code, new_course_name, new_college_code)

        # Redirect to the courses page or any other desired page
        return redirect('/courses')

    # Handle the GET request for displaying the edit form
    else:
        coursecode = request.args.get('coursecode')
        existing_course = get_existing_course(coursecode)

        if existing_course:
            course_name = existing_course['coursename']
            college_code = existing_course['collegecode']
            colleges = get_college()
            return render_template('editcourse.html', course_code=coursecode, course_name=course_name, college_code=college_code, colleges=colleges)
        else:
            return render_template('error.html', message="Course not found")
 


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
        delete_course(coursecode)
        return jsonify({'success': True})

