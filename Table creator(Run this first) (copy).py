import os
import sqlite3
#Creates the table
conn=sqlite3.connect('passwords.db')
p=conn.cursor()
p.execute("""CREATE TABLE passwords(Pass Text,
        website_or_app Text)""")
conn.commit()
conn.close()
print("Table created succesfully please close the program")
#Deletes file after table creation
os.remove(__file__)
