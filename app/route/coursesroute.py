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
        course_code = request.form['coursecode']
        course_name = request.form['coursename']
        college_code = request.form['collegecode']
        if check(course_code):
            flash('Course Code already exists!', 'error')
        elif len(course_code)> 20:
            flash('Course Code too long!', 'error')
        else:
            insert_course(course_code, course_name, college_code)
            return redirect('/courses') 
    colleges = get_college_codes()
    return render_template('addcourse.html', colleges=colleges)






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

