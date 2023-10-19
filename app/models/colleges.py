from flask_mysql_connector import MySQL 

mysql = MySQL()

def collegeread():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM colleges"
    cursor.execute(query)
    colleges = cursor.fetchall()
    cursor.close()
    return colleges

def add_col(collegecode, collegename):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO colleges (collegecode, collegename) VALUES (%s, %s)", (collegecode, collegename))
    mysql.connection.commit()
    cursor.close()

def find_colleges(searchcollege):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + searchcollege + "%"
    cursor.execute("SELECT * FROM colleges WHERE id LIKE %s OR firstname LIKE %s OR lastname LIKE %s OR coursecode LIKE %s OR yearlevel LIKE %s OR gender LIKE %s", (search_query, search_query, search_query, search_query, search_query, search_query))
    colleges = cursor.fetchall()
    cursor.close()
    return colleges

def find_colleges(college_search):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + college_search + "%"
    cursor.execute("SELECT * FROM colleges WHERE collegecode LIKE %s OR collegename LIKE %s", (search_query, search_query))
    colleges = cursor.fetchall()
    cursor.close()
    return colleges

def delete_college(college_code):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM colleges WHERE collegecode = %s", (college_code,))
    mysql.connection.commit()
    cursor.close()