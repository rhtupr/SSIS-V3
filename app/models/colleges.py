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
    
def update_college(collegecode, collegename):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE colleges SET collegename = %s WHERE collegecode = %s"
    cursor.execute(update_query, (collegename, collegecode))
    mysql.connection.commit()
    cursor.close()

def check(college_code):
    cursor = mysql.connection.cursor()
    query = "SELECT collegecode FROM colleges WHERE collegecode = %s"
    cursor.execute(query, (college_code,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return True

def insert_college(college_code, college_name):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO colleges (collegecode, collegename) VALUES (%s, %s)", (college_code, college_name))
    mysql.connection.commit()
    cursor.close()
        
