from configparser import ConfigParser
import os, sys
from src import database , svn
from datetime import datetime
import getpass

# read all data from .ini
config = ConfigParser()
config.read('.ini')
db = config.get('Database', 'database')
table = config.get('Database', 'table1')
repo_path = config.get('SVN', 'repopath')
work_path = config.get('SVN', 'workpath')
template = config.get('SVN', 'templatepath')

def main():

    if not os.path.exists(db):
        if not os.path.exists(os.path.dirname(db)):
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
                match action:
                    case '1':
                        # Do 1. Checkout an existing Project
                        print(1)
                    case '2':
                        # 2. Create a new Project
                        svn.new_entry(work_path, repo_path, template)
                        print(2)
                    case _:
                        continue
                print(action)
                break
        




if __name__ == '__main__':
    main()
    
