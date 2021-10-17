from configparser import ConfigParser
import os, sys
from src import database
from datetime import datetime
import getpass

# read all data from .ini
config = ConfigParser()
config.read('.ini')
db = config.get('Database', 'database')
table = config.get('Database', 'table1')
repo_path = config.get('SVN', 'repopath')
work_path = config.get('SVN', 'workpath')

def main():

    if not os.path.exists(db):
        os.mkdir(os.path.dirname(db))
        database.create_database(db, table)
        print(f'Database {db} succesfull created!')

    pass

    now = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    
    
    
    while True:
        #check which system is running and clean the console
        if sys.platform == 'linux':
            os.system('clear')
        else:
            os.system('cls')

        option_lst = ['1. Checkout an existing Project', '2. Create a new Project', 'q. Exit']
        print('What you will do? Please enter a value!','\n\t'.join([str(lst) for lst in option_lst]), sep='\n\t')
        
        action = input('\t')
        
        if action != '':
            if action in ['Q', 'q']:
                sys.exit()
            elif int(action) in range(len(option_lst)):
                
                print(action)
                break
        

def new_entry():

 
    # Check if the folder {work_path} exist if not create
    if not os.path.exists(work_path):
        os.makedirs(work_path)

    while True:
        vnum = input('Enter the V-Number: ')
        if not vnum == '':
            if len(vnum) == 11:
                break
    while True:
        custname = input('Enter the Customer Name: ')
        if not custname == '':
            break
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


if __name__ == '__main__':
    main()
    
