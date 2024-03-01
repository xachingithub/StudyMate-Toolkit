import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import subprocess
import os

class SpeechRecognitionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Speech Recognition App")
        self.master.geometry("400x200")
        
        self.label = tk.Label(master, text="Speak to execute a Python file:")
        self.label.pack()

        self.execute_button = tk.Button(master, text="Start Listening", command=self.listen_and_execute)
        self.execute_button.pack()

    def listen_and_execute(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            if "execute file" in command:
                # Extract the filename from the command
                filename = command.split("execute file")[-1].strip()
                
                # Check if the file exists with or without .py extension
                if os.path.exists(filename):
                    pass
                elif os.path.exists(filename + ".py"):
                    filename += ".py"
                else:
                    raise FileNotFoundError

                # Execute the Python file
                subprocess.Popen(["python", filename])

            else:
                messagebox.showinfo("Error", "Invalid command. Try again.")

        except sr.UnknownValueError:
            print("Could not understand audio")
            messagebox.showinfo("Error", "Could not understand audio. Try again.")
        except sr.RequestError as e:
            print("Error; {0}".format(e))
            messagebox.showinfo("Error", "Could not request results. Please check your internet connection.")
        except FileNotFoundError:
            print("File not found")
            messagebox.showinfo("Error", f"File {filename} not found.")

def main():
    root = tk.Tk()
    app = SpeechRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
