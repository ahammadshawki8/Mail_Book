import smtplib
from email.message import EmailMessage
import imghdr
from configuration import *


def send_email(to, subject, body, attachment_path = None, attachment_type = None):
    msg = EmailMessage()
    msg["From"] = USER_MAIL
    msg["To"]   = to
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment_path != None and attachment_type != None:
        if attachment_type == "image":
            with open(attachment_path, "rb") as pic:
                file_data = pic.read()
                file_name = pic.name
                file_type = imghdr.what(file_name)
            msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)
        elif attachment_type == "pdf":
            with open(attachment_path, "rb") as pdf:
                file_data = pdf.read()
                file_name = pdf.name
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
        elif attachment_type == "text":
            with open(attachment_path, "rb") as text:
                file_data = text.read()
                file_name = text.name
            msg.add_attachment(file_data, maintype="text", subtype="plain", filename=file_name)
        elif attachment_type == "csv":
            with open(attachment_path, "rb") as csv:
                file_data = csv.read()
                file_name = csv.name
            msg.add_attachment(file_data, maintype="text", subtype="csv", filename=file_name)
        else:
            return f"You can only attach {SUPPORTED_TYPES}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(USER_MAIL, USER_PASSWORD)
        smtp.send_message(msg)
    return "Email Sent"

