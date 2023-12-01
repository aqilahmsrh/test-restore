import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender_email = os.environ.get('SENDER_EMAIL')
receiver_email = os.environ.get('RECEIVER_EMAIL')
password = os.environ.get('PASSWORD_EMAIL')
requested_user = os.environ.get('REQUESTED_USER')

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = Header('Some Title', 'utf-8').encode()

body = f"Hi DevOps, your SIT MySQL DUmp is triggered; {workflow_link} by {requested_user}"

msg_content = MIMEText(body, 'plain', 'utf-8')
msg.attach(msg_content)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
