import os
import smtplib
from email.message import EmailMessage

def send_issue_solved_email():
    email_id = 'kumarraunak077@gmail.com'
    pswd = os.environ.get('password')
    email = EmailMessage()
    email['Subject'] = 'Issue Solved !!'
    email['From'] = email_id
    email['To'] = 'raunakraunak077@gmail.com'
    email.set_content('Check the file attached with this mail !!')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id ,pswd)
        smtp.send_message(email)
        print("Email Sent!!")
