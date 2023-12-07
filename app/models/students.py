from flask_mysql_connector import MySQL 

mysql = MySQL()

def studentread():
    cursor = mysql.connection.cursor(dictionary=True)
    query = """ SELECT students.*, CONCAT(colleges.collegename, ' (', courses.collegecode, ')') AS collegecode FROM students
    JOIN courses ON students.coursecode = courses.coursecode JOIN colleges ON courses.collegecode = colleges.collegecode"""    
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return students

def find_students(student_search):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + student_search + "%"
    query = """
        SELECT students.*, CONCAT(colleges.collegename, ' (', courses.collegecode, ')') AS collegecode
        FROM students
        JOIN courses ON students.coursecode = courses.coursecode
        JOIN colleges ON courses.collegecode = colleges.collegecode
        WHERE students.id LIKE %s
            OR students.firstname LIKE %s
            OR students.lastname LIKE %s
            OR students.coursecode LIKE %s
            OR students.yearlevel LIKE %s
            OR students.gender LIKE %s
            OR colleges.collegename LIKE %s
            OR colleges.collegecode LIKE %s
    """
    cursor.execute(query, (search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query))
    students = cursor.fetchall()
    cursor.close()
    return students


def delete_student(stud_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (stud_id,))
    mysql.connection.commit()
    cursor.close()

def update_student(student_id, first_name, last_name, course_code, year_level, gender, image_url):
    courses = get_course_codes()  # Fetch the course codes
    cursor = mysql.connection.cursor()
    update_query = "UPDATE students SET firstname = %s, lastname = %s, coursecode = %s, yearlevel = %s, gender = %s, image_url = %s WHERE id = %s"
    cursor.execute(update_query, (first_name, last_name, course_code, year_level, gender, image_url, student_id))
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
    query = "SELECT firstname, lastname, coursecode, yearlevel, gender, image_url FROM students WHERE id = %s"
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
    
def insert_student(student_id, first_name, last_name, course_code, year_level, gender, image_url):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO students (id, firstname, lastname, coursecode, yearlevel, gender, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s)", (student_id, first_name, last_name, course_code, year_level, gender, image_url))
    mysql.connection.commit()
    cursor.close()
    
def read_student(student_id):
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT students.id, students.firstname, students.lastname, students.yearlevel, students.gender, students.image_url, courses.coursecode, courses.coursename, colleges.collegecode, colleges.collegename FROM students JOIN courses ON students.coursecode = courses.coursecode JOIN colleges ON courses.collegecode = colleges.collegecode WHERE students.id = %s"
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()
    cursor.close()
    return result