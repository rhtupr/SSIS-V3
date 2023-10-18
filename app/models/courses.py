from flask_mysql_connector import MySQL 

mysql = MySQL()

def courseread():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM courses"
    cursor.execute(query)
    courses = cursor.fetchall()
    cursor.close()
    return courses


