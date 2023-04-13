import sqlite3
import random
import string

def insert_password(website, password):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords VALUES (?, ?)", (website, password))
    conn.commit()
    conn.close()

def generate_password(length, include_letters, include_digits, include_special_chars):
    letters = string.ascii_letters if include_letters else ''
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''
    chars = letters + digits + special_chars
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

default_password='password123'
conn = sqlite3.connect('passwords.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Password_key(password text)""")
c.execute("SELECT password FROM Password_key")
stored_password = c.fetchone()


if not stored_password:
    new_password=input('Set a password')
    c.execute("INSERT INTO Password_key VALUES (?)",(new_password,))
    conn.commit()
    stored_password=new_password
while True:
    entered_password=input("Enter the password to enter program:") 
    if entered_password!=stored_password[0]:
        print("Incorrect password")
    
    elif entered_password==stored_password[0]:
        break
    
while True:
    choice = input('1=Password manager, 2=Password generator, 3=Delete, 4=Exit\n')
    if choice == '1':
        sub_choice = input('1=Store password, 2=Show passwords\n')
        if sub_choice == '1':
            website = input('Enter website or app name:\n')
            password = input('Enter password:\n')
            insert_password(website, password)
        elif sub_choice == '2':
            conn = sqlite3.connect('passwords.db')
            c = conn.cursor()
            c.execute("SELECT rowid, * FROM passwords")
            passwords = c.fetchall()
            print("---------------------")
            print("ID"+"\t" + "Website" + "\t" + "Password")
            print("------------------------")    
            for p in passwords:
                print(str(p[0]) + '\t' + p[1] + '\t' + p[2])
            conn.close()


    elif choice == '2':
        include_letters = input('Do you want letters? y/n\n').lower() == 'y'
        include_digits = input('Do you want digits? y/n\n').lower() == 'y'
        include_special_chars = input('Do you want special characters? y/n\n').lower() == 'y'
        length = int(input('Enter password length:\n'))
        password = generate_password(length, include_letters, include_digits, include_special_chars)
        print('Generated password:', password)
        save_choice = input('Do you want to save the password? y/n\n').lower() == 'y'
        if save_choice:
            website = input('Enter website or app name:\n')
            insert_password(website, password)
    elif choice == '3':
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM passwords")
        passwords = c.fetchall()
        print("---------------------")
        print("ID"+"\t" + "Website" + "\t" + "Password")
        print("------------------------")    
        for p in passwords:
            print(str(p[0]) + '\t' + p[1] + '\t' + p[2])
        rowid = int(input('Enter rowid of password to delete:\n'))
        confirm = input(f"Are you sure you want to delete the password with ID {rowid}? y/n\n").lower() == 'y'
        if confirm:
            c.execute('DELETE FROM passwords WHERE rowid=?', (rowid,))
            conn.commit()
            conn.close()
            print('Password deleted successfully')
        else:
            print('Deletion cancelled')
    elif choice == '4':
        break
    else:
        print('Invalid choice, please try again')        #Hi how are yah?



        
             
        