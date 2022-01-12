# View instructions at README.md
import cv2
import numpy as np
import pyautogui
from pyngrok import ngrok
from datetime import datetime
from private_info import PHONE_NUMBER,TWILIO_NUMBER

def current_time():
    return str(datetime.now()).split()[1][:5]
    
def public_url():
    http_tunnel = ngrok.connect()
    return http_tunnel.public_url

def intervals(usage):    
    if usage == 'test':
        low, high = 5, 6
    if usage == 'real':
        max_minutes = 10
        seconds_per_minute = 60
        max_seconds = max_minutes*seconds_per_minute
        low, high = 60, max_seconds
    return low, high

def image(filename):
    image = pyautogui.screenshot() # take picture
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR) # not sure what this does
    cv2.imwrite(filename, image) # store image in file
    return filename

def img_url(url_stem,filename):
    img_url = f"{url_stem}/{filename}" # create address to access image
    return img_url

def send(client,body,img_url=None):
    client.messages.create(
        from_=f'whatsapp:+{TWILIO_NUMBER}',to=f"whatsapp:+{PHONE_NUMBER}",
        body=body,media_url=[img_url]) 