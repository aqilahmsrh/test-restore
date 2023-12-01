import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender_email = os.environ.get('SENDER_EMAIL')
receiver_email = os.environ.get('RECEIVER_EMAIL')
receiver_email_two = os.environ.get('RECEIVER_EMAIL_TWO')
password = os.environ.get('PASSWORD_EMAIL')
requested_user = os.environ.get('REQUESTED_USER')
workflow_link = os.environ.get('WORKFLOW_LINK')
env = os.environ.get('ENV')

receiver_emails = [os.environ.get('RECEIVER_EMAIL'), os.environ.get('RECEIVER_EMAIL_TWO')]

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = ', '.join(receiver_emails)
# msg['To'] = receiver_email
msg['Subject'] = Header('Some Title', 'utf-8').encode()

body = f"Hi DevOps, your {env} workflow for database dump is triggered; {workflow_link} by {requested_user}"

msg_content = MIMEText(body, 'plain', 'utf-8')
msg.attach(msg_content)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_emails, msg.as_string())
