from flask_mysql_connector import MySQL 

mysql = MySQL()

def courseread():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM courses"
    cursor.execute(query)
    courses = cursor.fetchall()
    cursor.close()
    return courses

def add_cou(coursecode, coursename, collegecode):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO courses (coursecode, coursename, collegecode) VALUES (%s, %s, %s)", (coursecode, coursename, collegecode))
    mysql.connection.commit()
    cursor.close()  


def find_courses(course_search):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + course_search + "%"
    cursor.execute("SELECT * FROM courses WHERE coursecode LIKE %s OR coursename LIKE %s OR collegecode LIKE %s", (search_query, search_query, search_query))
    courses = cursor.fetchall()
    cursor.close()
    return courses

def delete_course(course_code):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM courses WHERE coursecode = %s", (course_code,))
    mysql.connection.commit()
    cursor.close()
    
def update_course(course_code, new_course_name, new_college_code):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE courses SET coursename = %s, collegecode = %s WHERE coursecode = %s"
    cursor.execute(update_query, (new_course_name, new_college_code, course_code))
    mysql.connection.commit()
    cursor.close()


def get_college():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT collegecode FROM colleges"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_existing_course(coursecode):
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT coursename, collegecode FROM courses WHERE coursecode = %s"
    cursor.execute(query, (coursecode,))
    existing_course = cursor.fetchone()
    cursor.close()
    return existing_course

def check(course_code):
    cursor = mysql.connection.cursor()
    query = "SELECT coursecode FROM courses WHERE coursecode = %s"
    cursor.execute(query, (course_code,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return True

def insert_course(course_code, course_name, college_code):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO courses (coursecode, coursename, collegecode) VALUES (%s, %s, %s)", (course_code, course_name, college_code))
    mysql.connection.commit()
    cursor.close()
    
def get_college_codes():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT collegecode FROM colleges"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result