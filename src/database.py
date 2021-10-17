import sqlite3
import getpass
from datetime import datetime


def create_database(db, table):

    table = (f""" CREATE TABLE IF NOT EXISTS {table} (
                                            project_number TEXT,
                                            customer_name TEXT,
                                            machine_typ TEXT,
                                            branch TEXT,
                                            creator TEXT,
                                            date DATETIME
                                            );"""
             )

    sql_db = sqlite3.connect(db)
    cursor = sql_db.cursor()
    cursor.execute(table)
    sql_db.commit()
    sql_db.close()
    pass


def insert_database(db, table, in_value):

    in_value = in_value + (datetime.now().strftime("%Y/%m/%d, %H:%M:%S"),)

    insert = f"""INSERT INTO {table}
                            (project_number, customer_name, machine_typ, branch, creator, date)
                            VALUES (?,?,?,?,?,?);"""

    sql_db = sqlite3.connect(db)
    cursor = sql_db.cursor()
    cursor.execute(insert, in_value)
    sql_db.commit()
    sql_db.close()
    pass
