import sqlite3
import getpass


def create_database(db, table):

    table = (f""" CREATE TABLE IF NOT EXISTS {table} (
                                            Project_Number TEXT,
                                            Customer_Name TEXT,
                                            Machine_Typ TEXT,
                                            Branch TEXT,
                                            Creator TEXT,
                                            Date DATETIME
                                            );"""
                                            )

    sql_db = sqlite3.connect(db)
    cursor = sql_db.cursor()
    cursor.execute(table)
    sql_db.commit()
    sql_db.close()
    pass

def insert_database(db, in_value):
    
    insert = '''INSERT INTO '''

    pass
