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
