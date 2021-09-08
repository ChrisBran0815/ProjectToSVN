import pandas as pd
import requests
import numpy as np
import config
import os


URL = 'file:///home/christoph/Dokumente/Azure/ProjectToSVN/html/test.html'
username = config.username()
password = config.password()


def login():
    r = requests.get(URL, auth=(username, password))
    r.status_code


def writeREADME(df: pd.DataFrame, row):
    header = ['Vorgangs­nummerAbsteigend', 'Typ', 'Ersteller', 'Kunden­name',
              'Steuerung']
    dic = df.to_dict()
    keys = dic.keys()
    for key in keys:
        if not key == 'Vorgangs­nummerAbsteigend':
            print(key)
            if not os.path.exists('test/'):
                os.mkdir('test/')
            with open(f'test/README.md{row}', 'a') as thefile:
                thefile.write(f'#{key}:{dic.get(key)}\n')
    pass


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
    writeREADME(df=df.iloc[i], row=i+1)
    # # print(df.iloc[i,ii])

    # if os.path.exists('test/'):
    # writeREADME(df)
