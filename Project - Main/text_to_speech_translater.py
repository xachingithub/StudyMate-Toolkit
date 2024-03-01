from gtts import gTTS
from googletrans import Translator
import os
import tkinter as tk
from tkinter import filedialog

def text_to_speech(file_path, target_language='en'):
    with open(file_path, 'r') as file:
        text = file.read()

    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text

    # Prompt user for the output file name
    output_file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if output_file_name:
        # Save translated text to the specified txt file
        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            output_file.write(translated_text)

        # Convert translated text to speech
        tts = gTTS(translated_text, lang=target_language)
        audio_file_path = 'Audio/output_from_ttst.mp3'
        tts.save(audio_file_path)
        os.system('start ' + audio_file_path)

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a .txt file", filetypes=[("Text files", "*.txt")])
    if file_path:
        target_language = entry_language.get()  # Get the target language from the entry widget
        text_to_speech(file_path, target_language)

# Create the main window
window = tk.Tk()
window.title("Tranlater")
window.geometry("400x150")

# Create and configure the Open File button
open_button = tk.Button(window, text="Open File", command=open_file_dialog)
open_button.pack(pady=20)

# Create a Label and Entry for entering the target language
label_language = tk.Label(window, text="Enter Target Language Code:")
label_language.pack()

entry_language = tk.Entry(window)
entry_language.pack()

# Run the GUI application
window.mainloop()
