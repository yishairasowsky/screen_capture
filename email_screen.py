import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import time
import numpy as np
from private_info import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN, sender_email, receiver_email, sender_email_password
from functions import current_time, img_url,public_url,intervals,image,send

# usage = 'test'
usage = 'real'

low,high = intervals(usage)

while True:
    try:
        time.sleep(np.random.randint(low,high))
        filename = image('screen.png')
    except:
        pass

    message = MIMEMultipart()
    message["From"] = sender_email
    message['To'] = receiver_email
    # message['Subject'] = current_time()
    message['Subject'] = "Yishai's screen"
    file = "screen.png"
    attachment = open(file,'rb')
    obj = MIMEBase('application','octet-stream')
    obj.set_payload((attachment).read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition',"attachment; filename= "+file)
    message.attach(obj)
    my_message = message.as_string()
    email_session = smtplib.SMTP('smtp.gmail.com',587)
    email_session.starttls()
    email_session.login(sender_email,password=sender_email_password)
    email_session.sendmail(sender_email,receiver_email,my_message)
    email_session.quit()
    print(f"MAIL SENT at {current_time()}")
    pass

