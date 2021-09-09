import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('grace.thompson97@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Grace Thompson'
msg['To'] = 'basama4048@qqmimpi.com'
msg['Subject'] = 'Just a test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))
filename = 'code.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('grace.thompson97@gmail.com', 'basama4048@qqmimpi.com', text)