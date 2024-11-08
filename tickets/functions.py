import smtplib
from email.message import EmailMessage


def send_issue_status_email(user,ticketNo,status,raised_date):
    email_id = 'codersbuzz9@gmail.com'
    pswd = creaedoeycydpbnm
    email = EmailMessage()
    email['Subject'] = f'Issue #{ticketNo} {status} !!'
    email['From'] = email_id
    email['To'] = user
    email.set_content(f'Issue raised by {user} on {raised_date} by ticket number #{ticketNo} is {status}.')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id ,pswd)
        smtp.send_message(email)
        print("Email Sent!!")
