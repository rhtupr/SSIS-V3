from flask import * 
from app.models.students import *
from flask_wtf import *

students_bp = Blueprint ('students', __name__)

@students_bp.route('/students/')
def students():
    students = studentread()
    courses = get_course()  # Fetch the list of courses from your data source
    course_code = None  # Provide the selected course_code or set it based on some logic

    return render_template('students.html', students=students, courses=courses, course_code=course_code)

@students_bp.route('/students/add', methods=['GET', 'POST'])
def add_students():
    if request.method == 'POST':
        student_id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        gender = request.form['gender']
        add_stu(student_id, firstname, lastname, coursecode, yearlevel, gender)
        return redirect('/students')  # Redirect to the students page after adding a student

    # Fetch the list of courses to populate the coursecode dropdown
    courses = get_course()

    return render_template('addstudents.html', courses=courses)




@students_bp.route('/students/search', methods=['GET', 'POST'])
def search_students():
    students = []
    if request.method == 'POST':
        search_query = request.form.get('search_student')
        if search_query:
            students = find_students(search_query)
    return render_template('students.html', students=students)

@students_bp.route('/students/delete/<string:stud_id>', methods=['DELETE'])
def remove_student(stud_id):
    if request.method == 'DELETE':
        print(stud_id)
        delete_student(stud_id)
        return jsonify({'success': True})

@students_bp.route('/students/edit', methods=['POST'])
def edit_student():
    if request.method == 'POST':
        student_id = request.form.get('student_id')  # Get the student_id from the form
        first_name = request.form.get('first_name').title()
        last_name = request.form.get('last_name').title()
        course_code = request.form.get('course_code').upper()
        year_level = request.form.get('year_level')
        gender = request.form.get('gender').capitalize()
        update_student(student_id, first_name, last_name, course_code, year_level, gender)
        return redirect('/students/')
    

