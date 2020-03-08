import sqlite3
from os import path
import sys
import getpass
from login import *

# With db argument passed in, checks if it's a valid file. If valid connect and make cursor, if not print error and exit
db_name = sys.argv[1]
if path.exists(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
else:
    print("Error: Database not found.")
    exit()

#this is the main program loop, which will contain a logged in loop to make sure the user successfully logs in.
program_active = True
while program_active:
    user_email = input("Please enter your email or q to quit: ")
    if user_email == 'q':
        exit()
    if not('@' in user_email):
        print("Please enter a valid email.")
        continue
    user_pass = getpass.getpass(prompt='Please enter your password: ')
    logged_in = login(c, conn, user_email, user_pass)
    if not logged_in:
        print("Error: Unsuccessful login.")
        continue
    # or else do the normal stuff you'd do here.

# commit for the final time and then close the connection & finish the program
conn.commit()
conn.close()
