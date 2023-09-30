import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_mail():
    # Email and password (replace with your own)
    email_address = 'alexeyserdtse90@gmail.com'
    email_password = 'Aa15975368421!'

    # Create a connection to the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Gmail uses port 587 for TLS
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)

    # Start the TLS encryption
    smtp_connection.starttls()

    # Login to your Gmail account
    smtp_connection.login(email_address, email_password)

    # Compose the email message
    sender_email = email_address
    # Replace with the recipient's email address
    receiver_email = 'recipient_email@example.com'
    subject = 'Subject of the email'
    message_text = 'This is the body of the email.'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach a file (optional)
    file_path = 'path/to/attachment.pdf'
    attachment = open(file_path, 'rb')
    part = MIMEApplication(attachment.read(), Name='attachment.pdf')
    part['Content-Disposition'] = f'attachment; filename="{file_path}"'
    msg.attach(part)

    # Attach the message text
    msg.attach(MIMEText(message_text, 'plain'))

    # Send the email
    smtp_connection.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the SMTP connection
    smtp_connection.quit()
