import os, sys
import getpass
from datetime import datetime
from . import database
from tabulate import tabulate


def new_entry(work_path, repo_path, template):

    # Check if the folder {work_path} exist if not create
    # if not os.path.exists(work_path):
    #     os.makedirs(work_path)
    while True:
        #check which system is running and clean the console
        if sys.platform == 'linux':
            os.system('clear')
        else:
            os.system('cls')
            
        while True:
            vnum = input('Enter the V-Number: ')
            if not vnum == '':
                if len(vnum) == 11:
                    break
        while True:
            custname = input('Enter the Customer Name: ')
            if not custname == '':
                break
        while True:
            machine_typ = input('Enter the Machine Typ: ')
            if not machine_typ == '':
                break
        while True:
            branch = input('Enter the Branch: ')
            if not branch == '':
                break
        
        #check which system is running and clean the console
        if sys.platform == 'linux':
            os.system('clear')
        else:
            os.system('cls')

        print(tabulate([[vnum, custname, machine_typ, branch]], headers=['V-Number', 'Customer Name', 'Machine Type', 'Branch'], tablefmt='orgtbl'))
        in_right = input('Is your input correct? (Y/N): ')
        if in_right in ['Y', 'y']:
            break
        else: 
            continue
    sys.exit()
    projname = 'VT_' + vnum + '_' + custname.replace(' ', '_')
    work_path = work_path + '/' + projname
    new_project = repo_path + '/' + projname
    checkout = new_project + '/trunk'
    comment = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    comment = f'{comment} created by {getpass.getuser()}'
    print(new_project)
    os.system(f'svn mkdir "{new_project}" -m "{comment}"')
    os.system(
        f'svn import "{template}" "{new_project}" -m "Create Folder Structure"')
    os.system(f'svn checkout "{checkout}" "{work_path}"')
