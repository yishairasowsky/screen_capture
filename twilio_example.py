import cv2
import time
import numpy as np
import random
import pyautogui

from pyngrok import ngrok
from datetime import datetime
from twilio.rest import Client
from private_info import PHONE_NUMBER,TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

curr_time = str(datetime.now()).split()[1][:8]  


message = client.messages.create( 
    from_=f'whatsapp:+14155238886',
    body=f"Yishai's computer screen at {curr_time}.",      
    # media_url=[img_url],
    to=f"whatsapp:+{PHONE_NUMBER}",
    ) 

pass