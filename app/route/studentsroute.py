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

@students_bp.route('/students/edit', methods=['GET', 'POST'])
def edit_student():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        new_first_name = request.form.get('first_name').title()
        new_last_name = request.form.get('last_name').title()
        new_course_code = request.form.get('course_code').upper()
        new_year_level = request.form.get('year_level')
        new_gender = request.form.get('gender').capitalize()
        update_student(student_id, new_first_name, new_last_name, new_course_code, new_year_level, new_gender)
        return redirect('/students')
    else:
        student_id = request.args.get('student_id')
        existing_student = get_existing_student(student_id)

        if existing_student:
            first_name = existing_student['firstname']
            last_name = existing_student['lastname']
            course_code = existing_student['coursecode']
            year_level = existing_student['yearlevel']
            gender = existing_student['gender']
            return render_template('editstudent.html', student_id=student_id, first_name=first_name, last_name=last_name, course_code=course_code, year_level=year_level, gender=gender)
        else:
            return render_template('error.html', message="Student not found")