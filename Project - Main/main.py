import tkinter as tk
import os

def execute_python_file(file_path):
    try:
        if os.path.isfile(file_path):  # Check if the file path is valid
            os.system(f"python {file_path}")
        else:
            print(f"Invalid file path: {file_path}")
    except Exception as e:
        print(f"Error executing {file_path}: {e}")

def create_button(frame, button_name, file_path):
    button = tk.Button(frame, text=button_name, width=50, height=2, command=lambda: execute_python_file(file_path))
    button.pack(pady=5)

def main():
    root = tk.Tk()
    root.title("StudyMate Toolkit")

    # Set window icon
    icon_path = "C:/Sachin Sharma/Programming/Project - Main/Images/bag.ico"  # Replace with the actual path to your icon file
    if os.path.isfile(icon_path):
        root.iconbitmap(icon_path)

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    buttons_info = [
        ('Text to Speech', 'text_to_speech.py'),
        ('Translater', 'text_to_speech_translater.py'),
        ('Speech Recognition', 'sp_recon/speech_recon.py'),
        ('Send Email', 'send_mail.py')
    ]

    for button_name, file_path in buttons_info:
        create_button(frame, button_name, file_path)

    root.mainloop()

if __name__ == "__main__":
    main()
