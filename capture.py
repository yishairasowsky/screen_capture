# capture.py

# C:\Users\User\Documents\GitHub\screen_capture\env\Scripts\activate
# C:\Users\User\Downloads\ngrok-stable-windows-amd64\ngrok http 80
# py -m http.server 80

import os
import cv2
import time
import numpy as np
import pyautogui

from pyngrok import ngrok
from datetime import datetime
from twilio.rest import Client
from private_info import PHONE_NUMBER,TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN

# Open a HTTP tunnel on the default port 80
# <NgrokTunnel: "http://<public_sub>.ngrok.io" -> "http://localhost:80">
http_tunnel = ngrok.connect()
url = http_tunnel.public_url

PORT = 80

time_period = 60*5 # how many sec in 5 min 
import random

while True:
    n = random.randint(0,time_period)
    time.sleep(n)

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    cv2.imwrite("image1.png", image)

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)
    
    curr_time = str(datetime.now()).split()[1][:8]  

    img_url=f"{url}/image1.png"

    message = client.messages.create( 
        from_=f'whatsapp:+14155238886',
        body=f"Yishai's computer screenshot, sent to Shira at {curr_time}!",      
        media_url=[img_url],
        to=f"whatsapp:+{PHONE_NUMBER}",
        ) 