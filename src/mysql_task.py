import mysql.connector

def readData():
    print('hello')
    mycon = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Sol170701',
        database='Custom'
    )

    mycursor = mycon.cursor()

    mycursor.execute("SELECT * FROM Projects")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x[0])

def test1():
    mycon = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Sol170701'
    )

    mycursor = mycon.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase5")


    mycon = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Sol170701',
        database='mydatabase5'
    )

    mycursor = mycon.cursor()

    sql_table = """ CREATE TABLE IF NOT EXISTS Projects (
                                                Vorgangsnummer TEXT,
                                                Kundenname TEXT,
                                                Typ TEXT,
                                                Steuerung TEXT,
                                                Ersteller TEXT
                                                );"""

    mycursor.execute(sql_table)

if __name__ == '__main__':
    readData()