import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Sachin Sharma\Programming\Softwares\Tesseract\tesseract.exe'  # Modify this path as needed

# Function to extract text from image and save to a text file
def extract_text_and_save():
    # Get the path of the image file
    image_file_path = filedialog.askopenfilename(title="Select Image File",
                                                  filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if not image_file_path:
        messagebox.showerror("Error", "No image file selected.")
        return

    # Perform OCR using pytesseract
    try:
        image = Image.open(image_file_path)
        extracted_text = pytesseract.image_to_string(image)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return

    # Get the path of the text file to save
    text_file_path = filedialog.asksaveasfilename(title="Save Text As",
                                                   filetypes=[("Text files", "*.txt")],
                                                   defaultextension=".txt")
    if not text_file_path:
        messagebox.showerror("Error", "No text file selected.")
        return

    # Save the extracted text to the text file
    try:
        with open(text_file_path, "w") as file:
            file.write(extracted_text)
        messagebox.showinfo("Success", "Text extraction and saving completed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the text: {str(e)}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Image Text Extractor")
root.geometry("400x200")  # Set the initial size of the window

# Create a button to trigger text extraction and saving
extract_button = tk.Button(root, text="Extract Text from Image", command=extract_text_and_save)
extract_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
