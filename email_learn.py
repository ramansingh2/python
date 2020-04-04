from smtplib import SMTPException
import smtplib

sender = 'rs2244singh@gmail.com'
receivers = ['ramanrudra02@gmail.com']

message = """From: From Person <rs2244singh@gmail.com>
To: To Person <ramanrudra02@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except smtplib.SMTPException:
   print( "Error: unable to send email")