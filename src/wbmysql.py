import mysql.connector


mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='admin',
    passwd='Sol170701'
)

print(mydb)