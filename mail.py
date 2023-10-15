import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders

# Define the sender's and recipient's email addresses
sender_email = "yayainnovation3d@gmail.com"
receiver_email = "suryassuryas480@@gmail.com"

# Create a multipart message and set headers
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = "Test Email with Attachment"

# Add a body to the email
body = "This is the first line of the email.\n"
body += "This is the second line of the email.\n"
body += "This is the third line of the email."
message.attach(MIMEText(body, 'plain'))

# Attach a file
file_path = 'd:/exported_data.xlsx'  # Replace with the actual path to your file
attachment = MIMEApplication(open(file_path, 'rb').read())
attachment.add_header('Content-Disposition', 'attachment', filename='file.txt')
encoders.encode_base64(attachment)
message.attach(attachment)

# Connect to the SMTP server (in this case, using Gmail)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = "suryassuryas480@gmail.com"
#smtp_password = "yourpassword"

# Start TLS (Transport Layer Security) for secure connection
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Log in to your Gmail account
server.login(smtp_username) #, smtp_password)

# Send the message
server.sendmail(sender_email, receiver_email, message.as_string())

# Quit the server
server.quit()
