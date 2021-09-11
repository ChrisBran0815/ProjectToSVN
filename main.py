from configparser import ConfigParser
import sys
from src import crypto
from src import database
import os
from datetime import datetime
import time
from progress.bar import Bar

db = 'AWT.db'
table = ['projects', 'svn_path']
key = crypto.load_key('key.key')
ini = '.ini'

def progress(count, total, status=''):
    bar_len = 100
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush() 

def main():
    '''
    main script to write all Projects from V-Ablage to the database
    '''

    if not os.path.exists('key.key'):
        print('No key available.\nPlease ask your admin')
        input()
        sys.exit()

    if not os.path.exists(db):
        sql_tables = [""" CREATE TABLE IF NOT EXISTS Projects (
                                            Vorgangsnummer TEXT,
                                            Kundenname TEXT,
                                            Typ TEXT,
                                            Steuerung TEXT,
                                            Ersteller TEXT
                                            );""",
                      """ CREATE TABLE IF NOT EXISTS Members (
                                            GivenName TEXT,
                                            FamilieName TEXT,
                                            Email TEXT
                                            );"""
                      ]
        database.create_db(db)
        database.create_table(db, sql_tables)

    # Load the .ini Options
    config = ConfigParser()
    config.read(ini)

    # Set Username and Password
    user = config.get('Login Data', 'username')
    pwd = config.get('Login Data', 'passwd')
    
    #write the new .ini file
    config.set('Last Use', 'date', datetime.now().strftime("%Y/%m/%d, %H:%M:%S"))
    with open(ini, 'w') as configfile:
        config.write(configfile)

    
    '''
    
    here the code to work with the database
    
    '''

    print('End of Program')


if __name__ == '__main__':
    main()
    pass
