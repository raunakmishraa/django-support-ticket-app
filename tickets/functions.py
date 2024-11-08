import environ
import smtplib
from email.message import EmailMessage

env = environ.Env()
environ.Env.read_env()

def send_issue_status_email(user,ticketNo,status,raised_date):
    email_id = 'codersbuzz9@gmail.com'
    pswd = env('SENDER_EMAIL_PASS')
    email = EmailMessage()
    email['Subject'] = f'Issue #{ticketNo} {status} !!'
    email['From'] = email_id
    email['To'] = user
    email.set_content(f'Issue raised by {user} on {raised_date} by ticket number #{ticketNo} is {status}.')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id ,pswd)
        smtp.send_message(email)
        print("Email Sent!!")
