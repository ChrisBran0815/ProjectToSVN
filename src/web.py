import pandas as pd
import requests
import numpy as np
import config
import os
import sqlite3


URL = 'file:///home/christoph/Dokumente/Azure/ProjectToSVN/html/test.html'
username = config.username()
password = config.password()
DATABASE = 'projects.db'


def login():
    r = requests.get(URL, auth=(username, password))
    r.status_code


def writeDatabase(df: pd.DataFrame, row):
    header = ['Vorgangs­nummerAbsteigend', 'Typ', 'Ersteller', 'Kunden­name',
              'Steuerung']
    dic = df.to_dict()

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    sql_table = """ CREATE TABLE IF NOT EXISTS Projects (
                                            Vorgangsnummer TEXT,
                                            Kundenname TEXT,
                                            Typ TEXT,
                                            Steuerung TEXT,
                                            Ersteller TEXT
                                            );"""

    sql_query_insert = """INSERT INTO Projects
                          (Vorgangsnummer, Kundenname, Typ, Steuerung, Ersteller) 
                           VALUES (?, ?, ?, ?, ?);"""

    cursor.execute(sql_table)
    cursor.execute(sql_query_insert, (dic.get('Vorgangs­nummerAbsteigend'), dic.get('Kunden\xadname'), dic.get('Typ'), dic.get('Steuerung'), dic.get('Ersteller')))
    connection.commit()
    connection.close()

    # keys = dic.keys()
    # for key in keys:
    #         if not key == 'Vorgangs­nummerAbsteigend':
    #             print(key)
    #             if not os.path.exists('test/'):
    #                 os.mkdir('test/')
    #             with open(f'test/README.md{row}', 'a') as thefile:
    #                 thefile.write(f'#{key}:{dic.get(key)}\n')
    # pass


df = pd.read_html(URL)
df = df[0]
df = df.drop(columns=['Ampel',
                      'Alte Kundennamen',
                      'Status',
                      'Stich­wörter',
                      'Themen',
                      'Automation',
                      'Vertriebs­ingenieure',
                      'Land',
                      'Projekt-Nr',
                      'Maschinennr.',
                      'Unnamed: 0',
                      'Marktbetreuer',
                      'Vertriebs­gesellschaft',
                      'ELO-Pfad',
                      'Erstell­datum'
                      ], axis=1)
df.index = df.index + 1
df.index = df.index.rename('Index')




for i in range(len(df)):
    writeDatabase(df=df.iloc[i], row=i+1)
