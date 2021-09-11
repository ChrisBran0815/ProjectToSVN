import sqlite3

def create_db(db):
    '''
    creat an Sqllite Database if not exists
    '''
    sql_db = sqlite3.connect(db)

def create_table(db, sql_tables):

    sql_db =sqlite3.connect(db)
    cursor = sql_db.cursor()

    for sql_table in sql_tables:

        cursor.execute(sql_table)

    sql_db.commit()
    sql_db.close()
