from flask_mysql_connector import MySQL 

mysql = MySQL()

def studentread():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return students

def add_stu(id, firstname, lastname, coursecode, yearlevel, gender):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO students (id, firstname, lastname, coursecode, yearlevel, gender) VALUES (%s, %s, %s, %s, %s, %s)", (id, firstname, lastname, coursecode, yearlevel, gender))
    mysql.connection.commit()
    cursor.close()  

def find_students(student_search):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + student_search + "%"
    cursor.execute("SELECT * FROM students WHERE id LIKE %s OR firstname LIKE %s OR lastname LIKE %s OR coursecode LIKE %s OR yearlevel LIKE %s OR gender LIKE %s", (search_query, search_query, search_query, search_query, search_query, search_query))
    students = cursor.fetchall()
    cursor.close()
    return students

def delete_student(stud_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (stud_id,))
    mysql.connection.commit()
    cursor.close()

def update_student(student_id, first_name, last_name, course_code, year_level, gender):
    courses = get_course_codes()  # Fetch the course codes
    cursor = mysql.connection.cursor()
    update_query = "UPDATE students SET firstname = %s, lastname = %s, coursecode = %s, yearlevel = %s, gender = %s WHERE id = %s"
    cursor.execute(update_query, (first_name, last_name, course_code, year_level, gender, student_id))
    mysql.connection.commit()
    cursor.close()
    print(f"Student {student_id} updated with new data.")



def get_course():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT coursecode FROM courses"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
 
def get_existing_student(student_id):
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT firstname, lastname, coursecode, yearlevel, gender FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    existing_student= cursor.fetchone()
    cursor.close()
    return existing_student  

def get_course_codes():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT coursecode FROM courses"
    cursor.execute(query)
    course_code = cursor.fetchall()
    cursor.close()
    return course_code

def check(student_id):
    cursor = mysql.connection.cursor()
    query = "SELECT id FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return True
    
def insert_student(student_id, first_name, last_name, course_code, year_level, gender):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO students (id, firstname, lastname, coursecode, yearlevel, gender) VALUES (%s, %s, %s, %s, %s, %s)", (student_id, first_name, last_name, course_code, year_level, gender))
    mysql.connection.commit()
    cursor.close()