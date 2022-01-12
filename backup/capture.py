import time
import numpy as np
from private_info import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN
from twilio.rest import Client
from functions import current_time, img_url,public_url,intervals,image,send

url_stem = public_url()
# usage = 'test'
usage = 'real'
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
send(client=client,body=f"Connected to NGROK at {current_time()}.",img_url=img_url(url_stem=url_stem, filename='connected.jpg'))
low,high = intervals(usage)
while True:
    try:
        time.sleep(np.random.randint(low,high))
        filename = image('screen.png')
        send(client,body=f"Connected to NGROK at {current_time()}.",
            img_url=img_url(url_stem=url_stem,filename=filename))
    except:
        continue