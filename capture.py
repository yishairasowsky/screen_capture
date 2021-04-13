
# Python program to take
# screenshots
  
  
import numpy as np
import cv2
import pyautogui
   
  
# take screenshot using pyautogui
image = pyautogui.screenshot()
   
# since the pyautogui takes as a 
# PIL(pillow) and in RGB we need to 
# convert it to numpy array and BGR 
# so we can write it to the disk
image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
   
# writing it to the disk using opencv
cv2.imwrite("image1.png", image)

import os
from datetime import datetime

from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)
 
curr_time = str(datetime.now()).split()[1][:8]  

message = client.messages.create( 
    from_=f'whatsapp:+14155238886',
    
    body=f"Here my Yishai's current screenshot, photographed and sent to Shira at {curr_time}",      
    
    media_url=["https://6c89d8b24f96.ngrok.io/image1.png"],


    to=f"whatsapp:+{os.environ['PHONE_NUMBER']}"
                          ) 
 
print(message.sid)