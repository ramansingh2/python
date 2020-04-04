\
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("rs2244singh@gmail.com", "Ramanr@cks4")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("rs2244singh@gmail.com", "ramanrudra02@gmail.com", message)

# terminating the session
s.quit()