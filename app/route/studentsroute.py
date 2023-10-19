from flask import * 
from app.models.students import *
from flask_wtf import *

students_bp = Blueprint ('students', __name__)

@students_bp.route('/students/')
def students():
    students = studentread()
    return render_template('students.html', students=students)

@students_bp.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        gender = request.form['gender']
        print(student_id, firstname, lastname, coursecode, yearlevel, gender)
        add_stu(student_id, firstname, lastname, coursecode, yearlevel, gender)
        return redirect('/students')
    return render_template('students.html')

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


