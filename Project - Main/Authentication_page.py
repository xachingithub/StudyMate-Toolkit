import tkinter as tk
from tkinter import messagebox
import sqlite3
import bcrypt
import subprocess

# Initialize the SQLite database
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create a table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        app_code TEXT NOT NULL
    )
''')
conn.commit()

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

def show_sign_up():
    sign_in_frame.pack_forget()
    sign_up_frame.pack()

def show_sign_in():
    sign_up_frame.pack_forget()
    sign_in_frame.pack()

def sign_up():
    username = sign_up_username_entry.get()
    password = sign_up_password_entry.get()
    app_code = sign_up_app_code_entry.get()

    hashed_password = hash_password(password)

    # Check if the username already exists
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    if cursor.fetchone():
        messagebox.showerror('Error', 'Username already exists. Please choose a different one.')
        return

    # Insert user data into the database
    cursor.execute('INSERT INTO users (username, password, app_code) VALUES (?, ?, ?)',
                   (username, hashed_password, app_code))
    conn.commit()
    messagebox.showinfo('Success', 'Account created successfully!')

def sign_in():
    username = sign_in_username_entry.get()
    password = sign_in_password_entry.get()

    # Retrieve user data from the database
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    user_data = cursor.fetchone()

    if user_data and verify_password(password, user_data[2]):
        messagebox.showinfo('Success', 'Login successful!')
        # Run the Python file after successful login (replace 'your_file.py' with your file name)
        subprocess.run(['python', 'C:/Sachin Sharma/Programming/Project - Main/main.py'])
    else:
        messagebox.showerror('Error', 'Invalid username or password.')

# GUI setup
root = tk.Tk()
root.title('Sign In/Sign Up')
root.geometry("400x200")

sign_up_frame = tk.Frame(root, padx=10, pady=10)
sign_up_frame.pack_forget()

sign_in_frame = tk.Frame(root, padx=10, pady=10)

tk.Label(sign_up_frame, text='Username:').grid(row=0, column=0, sticky='w')
sign_up_username_entry = tk.Entry(sign_up_frame)
sign_up_username_entry.grid(row=0, column=1)

tk.Label(sign_up_frame, text='Password:').grid(row=1, column=0, sticky='w')
sign_up_password_entry = tk.Entry(sign_up_frame, show='*')
sign_up_password_entry.grid(row=1, column=1)

tk.Label(sign_up_frame, text='App Code:').grid(row=2, column=0, sticky='w')
sign_up_app_code_entry = tk.Entry(sign_up_frame)
sign_up_app_code_entry.grid(row=2, column=1)

sign_up_button = tk.Button(sign_up_frame, text='Sign Up', command=sign_up)
sign_up_button.grid(row=3, column=0, pady=5)

tk.Label(sign_in_frame, text='Username:').grid(row=0, column=0, sticky='w')
sign_in_username_entry = tk.Entry(sign_in_frame)
sign_in_username_entry.grid(row=0, column=1)

tk.Label(sign_in_frame, text='Password:').grid(row=1, column=0, sticky='w')
sign_in_password_entry = tk.Entry(sign_in_frame, show='*')
sign_in_password_entry.grid(row=1, column=1)

sign_in_button = tk.Button(sign_in_frame, text='Sign In', command=sign_in)
sign_in_button.grid(row=2, column=0, pady=5)

sign_up_option_button = tk.Button(root, text='Sign Up', command=show_sign_up)
sign_up_option_button.pack(pady=5)

sign_in_option_button = tk.Button(root, text='Sign In', command=show_sign_in)
sign_in_option_button.pack(pady=5)

root.mainloop()

# Close the database connection
conn.close()
