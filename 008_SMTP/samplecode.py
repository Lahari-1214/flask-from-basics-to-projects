# jdnk tqsr wmjr jdap

import smtplib
from email.message import EmailMessage
sender = 'sender email id'
receiver = 'receiver email id'
app_password = 'your app password' # generate app password from google account security settings

subject = "Application for Job"
body = '''
Dear Leela
Hope this message finds you well
regards
bla
bla.'''

msg = EmailMessage()
msg['subject'] = subject
msg['from']=sender
msg['to']=receiver
msg.set_content(body)

try:
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(sender,app_password)
        smtp.send_message(msg)
        print("Email sent successfully")
except Exception as e:
    print("Error sending email:",str(e))