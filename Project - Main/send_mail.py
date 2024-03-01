import tkinter as tk
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Add attachments
    for file_path in attached_files:
        attachment = open(file_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % file_path.split("/")[-1])
        msg.attach(part)

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        result_label.config(text="Email sent successfully!", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

def attach_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        attached_files.append(file_path)
        attached_files_label.config(text=f"Attached files: {', '.join(attached_files)}")

# GUI setup
root = tk.Tk()
root.title("Email Sender")

# Sender's Email and Password
tk.Label(root, text="Sender's Email:").pack()
sender_email_entry = tk.Entry(root)
sender_email_entry.pack()

tk.Label(root, text="Sender's Password:").pack()
sender_password_entry = tk.Entry(root, show="*")
sender_password_entry.pack()

# Recipient's Email
tk.Label(root, text="Recipient's Email:").pack()
recipient_email_entry = tk.Entry(root)
recipient_email_entry.pack()

# Subject
tk.Label(root, text="Subject:").pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

# Body
tk.Label(root, text="Body:").pack()
body_text = tk.Text(root, height=5, width=50)
body_text.pack()

# Attach Files
attached_files = []
tk.Button(root, text="Attach File", command=attach_file).pack()
attached_files_label = tk.Label(root, text="Attached files: None")
attached_files_label.pack()

# Send Button
tk.Button(root, text="Send Email", command=send_email).pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
