import tkinter as tk
from tkinter import Button, Label, Text, Scrollbar, Toplevel, Entry, filedialog
import speech_recognition as sr

class SpeechRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech Recognition App")

        self.label = Label(root, text="Click 'Recognize Speech' to start recording.")
        self.label.pack(pady=10)

        self.textbox = Text(root, height=10, width=50, wrap=tk.WORD)
        self.textbox.pack(pady=10)

        self.scrollbar = Scrollbar(root, command=self.textbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.textbox.config(yscrollcommand=self.scrollbar.set)

        self.recognize_button = Button(root, text="Recognize Speech", command=self.recognize_speech)
        self.recognize_button.pack(pady=10)

        self.save_button = Button(root, text="Save to File", command=self.save_to_file)
        self.save_button.pack(pady=10)

    def recognize_speech(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.label.config(text="Recording... Speak now!")
            self.root.update()
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            self.label.config(text="Speech recognition successful.")
            self.textbox.insert(tk.END, text + '\n')
        except sr.UnknownValueError:
            self.label.config(text="Sorry, could not understand audio.")
        except sr.RequestError as e:
            self.label.config(text=f"Could not request results from Google Speech Recognition service; {e}")

    def save_to_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt")],
                                                    title="Select file to save")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.textbox.get("1.0", tk.END))
            self.label.config(text=f"Recognized text saved to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechRecognitionApp(root)
    root.mainloop()
