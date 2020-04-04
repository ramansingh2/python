import smtplib
sender="rs2244singh@gmail.com"
receiver="ramanrudra02@gmail.com"
password=input(str("enter your passwd:"))
message="hello this is raman singh"

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
print("login successfull")
server.sendmail(sender,receiver,message)
print("email has been sent to ",receiver)