import os
import cv2
import numpy as np
import pyautogui

from datetime import datetime
from twilio.rest import Client


image = pyautogui.screenshot()
   
image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
   
cv2.imwrite("image1.png", image)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)
 
curr_time = str(datetime.now()).split()[1][:8]  

message = client.messages.create( 
    from_=f'whatsapp:+14155238886',
    body=f"Yishai's computer screenshot, sent to Shira at {curr_time}!",      
    media_url=["https://6c89d8b24f96.ngrok.io/image1.png"],
    to=f"whatsapp:+{os.environ['PHONE_NUMBER']}",
                          ) 