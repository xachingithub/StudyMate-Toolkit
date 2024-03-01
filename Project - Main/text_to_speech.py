from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog

def text_to_speech(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    tts = gTTS(text, lang='en')
    audio_file_path = 'Audio/output_from_tts.mp3'
    tts.save(audio_file_path)
    os.system('start ' + audio_file_path)

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a .txt file", filetypes=[("Text files", "*.txt")])
    if file_path:
        text_to_speech(file_path)

# Create the main window
window = tk.Tk()
window.title("Text-to-Speech Converter")
window.geometry("400x150")

# Create and configure the Open File button
open_button = tk.Button(window, text="Open File", command=open_file_dialog)
open_button.pack(pady=50)

# Run the GUI application
window.mainloop()
