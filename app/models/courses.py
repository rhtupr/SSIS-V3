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


