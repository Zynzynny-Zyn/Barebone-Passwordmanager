import sqlite3

conn=sqlite3.connect('passwords.db')
c=conn.cursor()
c.execute("SELECT * FROM Password_key")
stored_password = c.fetchone()
print(stored_password[0])
